# Count the steps each search needs
def linear_search(items, target):
    steps = 0
    for i, value in enumerate(items):
        steps += 1
        if value == target:
            return i, steps
    return -1, steps

def binary_search(items, target):
    low, high, steps = 0, len(items) - 1, 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if items[mid] == target:
            return mid, steps
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

codes = list(range(0, 2_000_000, 2))   # sorted codes
target = 1_765_432
print("linear:", linear_search(codes, target))
print("binary:", binary_search(codes, target))
