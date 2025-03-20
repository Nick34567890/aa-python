"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choosing the pivot as the middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
"""
import random
import time
import matplotlib.pyplot as plt

comparisons = 0
swaps = 0

def quicksort_with_metrics(arr, low, high):
    global comparisons, swaps
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort_with_metrics(arr, low, pi - 1)
        quicksort_with_metrics(arr, pi + 1, high)

def partition(arr, low, high):
    global comparisons, swaps
    pivot = arr[high]  # pivot element
    i = low - 1  # index of smaller element

    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            swaps += 1
            print(f"Array after swap {swaps}: {arr}")  # Print array after each swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element
    swaps += 1
    print(f"Array after swap {swaps}: {arr}")  # Print array after this final swap

    return i + 1

def print_in_chunks(arr, chunk_size=10):
    """Helper function to print the array in chunks of `chunk_size`."""
    for i in range(0, len(arr), chunk_size):
        print(arr[i:i + chunk_size])

def run_performance_tests():
    array_sizes = list(range(10, 101, 10))  # Array sizes from 10 to 100 (in steps of 10)
    execution_times = []

    for size in array_sizes:
        # Generate a random array of 'size' elements
        arr = [random.randint(1, 1000) for _ in range(size)]

        # Reset global counters
        global comparisons, swaps
        comparisons, swaps = 0, 0

        # Time the sorting process
        start_time = time.time()
        quicksort_with_metrics(arr, 0, len(arr) - 1)  # Sort the array
        end_time = time.time()

        execution_times.append(end_time - start_time)  # Store execution time

    return array_sizes, execution_times

# Run performance tests for multiple array sizes
array_sizes, execution_times = run_performance_tests()

# Plot the performance metrics (execution times vs. array sizes)
plt.figure(figsize=(10, 6))

# Plot Execution Time vs Array Size
plt.plot(array_sizes, execution_times, label="Execution Time", marker='o', color='blue')
plt.title('Execution Time vs Array Size for Quicksort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')

# Display the plot
plt.legend()
plt.grid(True)
plt.show()









