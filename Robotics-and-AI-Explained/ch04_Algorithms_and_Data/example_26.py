# Insertion sort: like sorting playing cards in hand
def insertion_sort(items):
    items = items[:]            # work on a copy
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j] > current:
            items[j + 1] = items[j]   # shift right
            j -= 1
        items[j + 1] = current
    return items

battery_levels = [72, 15, 98, 43, 60, 8, 85]
print("sorted:", insertion_sort(battery_levels))
print("python:", sorted(battery_levels))
print("lowest three:", sorted(battery_levels)[:3])
