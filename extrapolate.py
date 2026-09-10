import pandas as pd
import math

RESULTS_CSV = 'sort_benchmark_results.csv'
TOTAL_ROWS = 28_374_211  # <-- fill this in with your Part A total row count (numeric column, non-missing count is fine too)

df = pd.read_csv(RESULTS_CSV)

# Use the largest sample size, random ordering, ARR_DELAY column, to estimate c
largest_n = df['size'].max()
subset = df[(df['size'] == largest_n) & (df['ordering'] == 'random') & (df['column'] == 'ARR_DELAY')]

print(f'Using n={largest_n} (largest sample) to fit c for time = c * n^2\n')

results = {}
for _, row in subset.iterrows():
    algo = row['algorithm']
    t = row['time_seconds']
    c = t / (largest_n ** 2)
    results[algo] = c
    print(f'{algo}: measured time={t:.6f}s at n={largest_n}  ->  c = {c:.3e}')

def format_duration(seconds):
    """Convert seconds into the most readable unit."""
    minute, hour, day, year = 60, 3600, 86400, 31_536_000
    if seconds < minute:
        return f'{seconds:.2f} seconds'
    elif seconds < hour:
        return f'{seconds/minute:.2f} minutes'
    elif seconds < day:
        return f'{seconds/hour:.2f} hours'
    elif seconds < year:
        return f'{seconds/day:.2f} days'
    else:
        return f'{seconds/year:.2f} years'

if TOTAL_ROWS is None:
    raise ValueError('Set TOTAL_ROWS to your Part A total row count before running this.')

print(f'\nExtrapolating to full dataset size: {TOTAL_ROWS:,} rows\n')

full_scale_estimates = {}
for algo, c in results.items():
    est_seconds = c * (TOTAL_ROWS ** 2)
    full_scale_estimates[algo] = est_seconds
    print(f'{algo}: estimated time at full scale = {format_duration(est_seconds)}')

# Compare against Timsort O(n log n) - estimate its constant from the SAME largest-n measurement
# using Python's actual sorted() on that same sample size for a fair constant
import time
import numpy as np
rng = np.random.default_rng(42)
sample_for_timsort = rng.integers(-100, 100, size=largest_n).tolist()

start = time.perf_counter()
sorted(sample_for_timsort)
end = time.perf_counter()
timsort_measured = end - start

c_timsort = timsort_measured / (largest_n * math.log2(largest_n))
timsort_full_seconds = c_timsort * (TOTAL_ROWS * math.log2(TOTAL_ROWS))

print(f'\nPython sorted() (Timsort) at n={largest_n}: {timsort_measured:.6f}s')
print(f'Estimated Timsort time at full scale: {format_duration(timsort_full_seconds)}')

print('\nSpeedup factor (O(n^2) algorithm time / Timsort time) at full scale:')
for algo, est_seconds in full_scale_estimates.items():
    speedup = est_seconds / timsort_full_seconds
    print(f'{algo}: Timsort is ~{speedup:,.0f}x faster')