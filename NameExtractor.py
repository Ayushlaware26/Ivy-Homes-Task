import requests
import time
from collections import deque


class NameExtractor:
    def __init__(self, api_url, api_version):
        self.api_url = api_url
        self.api_version = api_version
        self.explored = set()
        self.queue = deque()
        self.collected_names = set()
        self.request_count = 0

    def get_completions(self, query):
        endpoint = f"{self.api_url}/{self.api_version}/autocomplete?query={query}"
        try:
            response = requests.get(endpoint)
            self.request_count += 1
            if response.status_code == 200:
                return response.json().get('results', [])
            else:
                print(f"Failed to fetch '{query}' from {self.api_version}: HTTP {response.status_code}")
                return []
        except Exception as error:
            print(f"Error fetching '{query}' from {self.api_version}: {error}")
            return []

    def gather_names(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.queue.append(char)
            self.explored.add(char)

        while self.queue:
            current_query = self.queue.popleft()
            results = self.get_completions(current_query)
            time.sleep(0.1)

            for name in results:
                if name not in self.collected_names:
                    self.collected_names.add(name)
                    extended_query = name[:len(current_query) + 1]

                    if extended_query not in self.explored:
                        self.explored.add(extended_query)
                        self.queue.append(extended_query)

        return sorted(self.collected_names)


if __name__ == "__main__":
    api_url = "http://35.200.185.69:8000"
    versions = ["v1", "v2", "v3"]
    extraction_summary = {}

    for version in versions:
        print(f"Starting extraction for version {version}...")
        extractor = NameExtractor(api_url, version)
        extracted_names = extractor.gather_names()

        extraction_summary[version] = {
            "name_count": len(extracted_names),
            "requests_made": extractor.request_count,
            "names": extracted_names
        }

        print(f"Completed version {version}:")
        print(f"Names found: {len(extracted_names)}")
        print(f"API requests made: {extractor.request_count}")

    print("\nOverall Summary:")
    for ver, data in extraction_summary.items():
        print(f"{ver.upper()}:")
        print(f"- Names Extracted: {data['name_count']}")
        print(f"- API Requests: {data['requests_made']}")
