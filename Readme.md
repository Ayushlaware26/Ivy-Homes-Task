# Autocomplete API Extraction (v1, v2, v3)

## Overview

This project aims to extract possible names from an autocomplete API across three versions: `v1`, `v2`, and `v3`. The API endpoint follows the pattern:

```
http://35.200.185.69:8000/{version}/autocomplete?query=<string>
```

The approach used here is heuristic — it is not exhaustive but aims to cover a substantial portion of possible names while adhering to practical constraints.

---

## Approach

### 1. **Exploration**

- The endpoints `/v1/autocomplete`, `/v2/autocomplete`, and `/v3/autocomplete` were queried using incremental prefixes.
- Each request returns a JSON object with a `results` array containing matching names.
- An empty response signals a terminal point for that prefix.


### 2. **Algorithm**

- Utilized a **Breadth-First Search (BFS)** strategy for systematic exploration:
    - Start with all lowercase letters (`a-z`) as initial prefixes.
    - Query the API for each prefix and collect results.
    - Extend valid prefixes incrementally until no new results are found.
- Employed sets for efficient tracking of visited prefixes and discovered names.


### 3. **Optimizations**

- Added a delay of 100ms between requests to prevent server overload.
- This heuristic approach does not guarantee capturing all possible names but aims to extract a significant portion efficiently.

---

## Findings

### Results Summary

| Version | Total API Requests | Unique Names Found |
| :-- | :-- | :-- |
| v1 | **52** | **260** |
| v2 | **104** | **329** |
| v3 | **134** | **411** |

### Observations

1. **Prefix-based Completion**: Names are identified by extending valid prefixes.
2. **Rate Limiting**: No explicit rate limiting encountered; a delay is included as a precaution.

---

## How to Run

### Prerequisites

1. Python 3.x should be installed.
2. Install the required library:

```
pip install requests
```


### Steps

1. Save the script as `autocomplete_extractor_v123.py`.
2. Execute the script:

```
python autocomplete_extractor_v123.py
```

Results for each version (`v1`, `v2`, `v3`) will be displayed on completion.

---

## Results

- Total API requests made for each version.
- Unique names extracted for each version.

---

## File Structure

```
autocomplete_extractor_v123.py   # Python script for extracting names from v1, v2, and v3
README.md                        # Documentation explaining the approach and findings
```

---

## Metrics

| Metric | v1 | v2 | v3 |
| :-- | :-- | :-- | :-- |
| Total API Requests | 52 | 104 | 134 |
| Unique Names Extracted | 260 | 329 | 411 |

---

## Notes

- This heuristic approach can be extended to handle additional versions if needed.
- Ensure a stable internet connection while running the script, as multiple API requests are made.
