# Autocomplete API Extraction (v1, v2, v3)

## Overview

This project aims to extract possible names from an autocomplete API across three versions: `v1`, `v2`, and `v3`. The approach is heuristic, focusing on covering a significant portion of possible names without guaranteeing complete extraction.

### Approach

- **Heuristic and BFS Exploration:**
  - The extraction follows a **Breadth-First Search (BFS)** approach, starting with all lowercase letters (`a-z`) as initial prefixes.
  - Valid prefixes are extended incrementally, and results are collected until no new names are discovered.
  - The approach prioritizes efficiency over exhaustiveness, making it practical for large datasets.

- **Optimizations:**
  - A delay of 100ms is applied between requests to minimize server strain.
  - Sets are used for efficient tracking of visited prefixes and discovered names.

### Results Summary

| Version | Total API Requests | Unique Names Found |
| :-- | :-- | :-- |
| v1 | **52** | **260** |
| v2 | **104** | **329** |
| v3 | **134** | **411** |

### Notes

- This heuristic approach can be adapted for additional versions if required.
- Ensure a stable internet connection while running the script, as multiple API requests are involved.
