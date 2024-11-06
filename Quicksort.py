import random
import time
import sys

# Increase the recursion limit to 6000
sys.setrecursionlimit(6000)

# Randomized partition function for quicksort
def randomized_partition(arr, low, high):
    # Select a random pivot and swap it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    # Partition the array around the pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized quicksort function
def randomized_quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = randomized_partition(arr, low, high)
        # Recursively sort the subarrays
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Edge cases: empty array, sorted array, reverse-sorted array, array with duplicates
test_cases = [
    [],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [5, 3, 4, 3, 3]
]

# Test the randomized quicksort with edge cases
for i, case in enumerate(test_cases):
    randomized_quicksort(case, 0, len(case) - 1)
    print(f"Sorted result for test case {i+1}: {case}")

# Deterministic partition function for quicksort (pivot is the first element)
def deterministic_partition(arr, low, high):
    pivot = arr[low]  # First element as pivot
    i = low + 1  # Start from the next element
    # Compare all elements with pivot
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:  # If element is smaller than pivot, swap it with arr[i]
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Move pivot to its correct position
    return i - 1  # Return the partition index

# Deterministic quicksort function
def deterministic_quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = deterministic_partition(arr, low, high)
        # Ensure that both subarrays have elements to process
        if pi - 1 > low:
            deterministic_quicksort(arr, low, pi - 1)  # Recursively sort the left subarray
        if pi + 1 < high:
            deterministic_quicksort(arr, pi + 1, high)  # Recursively sort the right subarray

# Test the deterministic quicksort and measure time
def test_deterministic_quicksort():
    input_sizes = [100, 1000]
    test_distributions = {
        "Random": lambda size: [random.randint(1, 100) for _ in range(size)],
        "Sorted": lambda size: list(range(size)),
        "Reverse-Sorted": lambda size: list(range(size, 0, -1)),
        "Repeated Elements": lambda size: [random.choice([1, 2, 3]) for _ in range(size)]
    }

    for size in input_sizes:
        for dist_name, dist_func in test_distributions.items():
            arr = dist_func(size)

            # Deterministic Quicksort timing
            arr_copy = arr[:]
            start = time.time()
            deterministic_quicksort(arr_copy, 0, len(arr_copy) - 1)
            det_quick_time = time.time() - start

            print(f"Size: {size}, Distribution: {dist_name}, Deterministic Quicksort: {det_quick_time:.6f} seconds")

# Run the test
test_deterministic_quicksort()