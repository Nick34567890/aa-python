import random
import time
import matplotlib.pyplot as plt

comparisons = 0
swaps = 0

def merge_sort_with_metrics(arr):
    global comparisons, swaps
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left = arr[:mid]  # Divide the array into two halves
        right = arr[mid:]

        merge_sort_with_metrics(left)  # Sort the first half
        merge_sort_with_metrics(right)  # Sort the second half

        i = j = k = 0

        # Merging the two halves
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            print(f"Array after merge step {k}: {arr}")  # Print array after each merge step

        # If there are any elements left in the left or right half, add them
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

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
        merge_sort_with_metrics(arr)  # Sort the array using MergeSort
        end_time = time.time()

        execution_times.append(end_time - start_time)  # Store execution time

    return array_sizes, execution_times

# Run performance tests for multiple array sizes
array_sizes, execution_times = run_performance_tests()

# Plot the performance metrics (execution times vs. array sizes)
plt.figure(figsize=(10, 6))

# Plot Execution Time vs Array Size
plt.plot(array_sizes, execution_times, label="Execution Time", marker='o', color='blue')
plt.title('Execution Time vs Array Size for MergeSort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')

# Display the plot
plt.legend()
plt.grid(True)
plt.show()
