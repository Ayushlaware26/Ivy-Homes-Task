import requests
import time
from collections import deque


class NameExtractor:
    def __init__(self, base_url, version):
        self.base_url = base_url
        self.version = version
        self.visited = set()
        self.queue = deque()
        self.found_names = set()
        self.request_count = 0

    def fetch_names(self, query):
        url = f"{self.base_url}/{self.version}/autocomplete?query={query}"
        try:
            response = requests.get(url)
            self.request_count += 1
            if response.status_code == 200:
                return response.json().get('results', [])
            else:
                print(f"Error {response.status_code} for query '{query}' on {self.version}")
                return []
        except Exception as e:
            print(f"Exception for query '{query}' on {self.version}: {e}")
            return []

    def extract_names(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.queue.append(char)
            self.visited.add(char)

        while self.queue:
            current = self.queue.popleft()
            results = self.fetch_names(current)
            time.sleep(0.1)

            for name in results:
                if name not in self.found_names:
                    self.found_names.add(name)
                    next_prefix = name[:len(current) + 1]

                    if next_prefix not in self.visited:
                        self.visited.add(next_prefix)
                        self.queue.append(next_prefix)

        return sorted(self.found_names)


if __name__ == "__main__":
    base_url = "http://35.200.185.69:8000"
    versions = ["v1", "v2", "v3"]
    summary = {}

    for version in versions:
        print(f"Extracting for version {version}...")
        extractor = NameExtractor(base_url, version)
        names = extractor.extract_names()

        summary[version] = {
            "total_names": len(names),
            "api_requests": extractor.request_count,
            "names": names
        }

        print(f"Version {version} completed:")
        print(f"- Total Names: {len(names)}")
        print(f"- API Requests: {extractor.request_count}")

    print("\nSummary of Results:")
    for ver, data in summary.items():
        print(f"{ver.upper()}:")
        print(f"- Names Found: {data['total_names']}")
        print(f"- Requests Made: {data['api_requests']}")
