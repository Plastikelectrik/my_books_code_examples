# Time a linear and a quadratic algorithm
import time

def has_duplicates_slow(items):       # O(n^2)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

def has_duplicates_fast(items):       # O(n)
    return len(set(items)) != len(items)

for n in [1000, 2000, 4000]:
    data = list(range(n))
    t0 = time.perf_counter()
    has_duplicates_slow(data)
    t1 = time.perf_counter()
    has_duplicates_fast(data)
    t2 = time.perf_counter()
    print(f"n={n}: slow {t1 - t0:.3f} s, "
          f"fast {t2 - t1:.5f} s")
