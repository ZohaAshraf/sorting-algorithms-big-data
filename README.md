markdown
# Sorting Algorithms on Real-World Big Data

Implementation and empirical benchmarking of three classic O(n²) sorting
algorithms — Bubble Sort, Selection Sort, and Insertion Sort — built from
scratch and tested against a real-world, multi-gigabyte dataset.

## Overview

This project explores why quadratic-time sorting algorithms break down at
scale. Using the Airline Delay and Cancellation dataset (2009–2018, ~7GB),
it benchmarks all three algorithms across multiple sample sizes and input
orderings (random, sorted, reversed), then extrapolates the measured
runtimes to estimate how long a full-scale sort would actually take.

## Dataset

[Airline Delay and Cancellation Data, 2009–2018](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018)
— U.S. domestic flight records, loaded in chunks via pandas.

## Project Structure

├── explore_data.py # Data loading & exploration (Part A)
├── sort_algorithms.py # Bubble, Selection & Insertion sort implementations
├── benchmark.py # Sampling, timing, and CSV export of results
├── data/ # Raw CSVs (not tracked in git)
├── results/ # sort_benchmark_results.csv
├── charts/ # Runtime comparison plots
└── report/ # Written analysis (PDF/Word)


## Setup

```bash
python -m venv venv
venv\Scripts\activate       # Windows
pip install pandas kaggle matplotlib
```

## Key Findings

*(to be filled in after Part E — a one-line summary of the extrapolated
full-scale runtime and the O(n²) vs O(n log n) speedup factor)*

## Author

Zoha Ashraf — BS Computer Science, FAST-NUCES