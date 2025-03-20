import random
import time
import matplotlib.pyplot as plt

comparisons = 0
swaps = 0

def bubble_sort_with_metrics(arr):
    global comparisons, swaps
    n = len(arr)

    # Bubble Sort logic
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swaps += 1
                print(f"Array after swap {swaps}: {arr}")  # Print array after each swap

def print_in_chunks(arr, chunk_size=10):
    """Helper function to print the array in chunks of `chunk_size`."""
    for i in range(0, len(arr), chunk_size):
        print(arr[i:i + chunk_size])

def run_performance_tests():
    array_sizes = list(range(10, 40, 10))  # Array sizes from 10 to 100 (in steps of 10)
    execution_times = []

    for size in array_sizes:
        # Generate a random array of 'size' elements
        arr = [random.randint(1, 1000) for _ in range(size)]

        # Reset global counters
        global comparisons, swaps
        comparisons, swaps = 0, 0

        # Time the sorting process
        start_time = time.time()
        bubble_sort_with_metrics(arr)  # Sort the array using BubbleSort
        end_time = time.time()

        execution_times.append(end_time - start_time)  # Store execution time

    return array_sizes, execution_times

# Run performance tests for multiple array sizes
array_sizes, execution_times = run_performance_tests()

# Plot the performance metrics (execution times vs. array sizes)
plt.figure(figsize=(10, 6))

# Plot Execution Time vs Array Size
plt.plot(array_sizes, execution_times, label="Execution Time", marker='o', color='blue')
plt.title('Execution Time vs Array Size for BubbleSort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')

# Display the plot
plt.legend()
plt.grid(True)
plt.show()

