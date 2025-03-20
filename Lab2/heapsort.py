import random
import time
import matplotlib.pyplot as plt

comparisons = 0
swaps = 0

def heapify(arr, n, i):
    global comparisons, swaps
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Compare left child with root
    comparisons += 1
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare right child with root
    comparisons += 1
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        swaps += 1
        print(f"Array after swap {swaps}: {arr}")  # Print array after each swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort_with_metrics(arr):
    global comparisons, swaps
    n = len(arr)

    # Build a max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        swaps += 1
        print(f"Array after swap {swaps}: {arr}")  # Print array after each swap
        heapify(arr, i, 0)  # Heapify the root

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
        heap_sort_with_metrics(arr)  # Sort the array using HeapSort
        end_time = time.time()

        execution_times.append(end_time - start_time)  # Store execution time

    return array_sizes, execution_times

# Run performance tests for multiple array sizes
array_sizes, execution_times = run_performance_tests()

# Plot the performance metrics (execution times vs. array sizes)
plt.figure(figsize=(10, 6))

# Plot Execution Time vs Array Size
plt.plot(array_sizes, execution_times, label="Execution Time", marker='o', color='blue')
plt.title('Execution Time vs Array Size for HeapSort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')

# Display the plot
plt.legend()
plt.grid(True)
plt.show()
