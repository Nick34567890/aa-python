import random
import time
import matplotlib.pyplot as plt

# QuickSort Implementation
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

# MergeSort Implementation
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# HeapSort Implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# BubbleSort Implementation
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Function to generate random array of given size
def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Function to measure time for each sorting algorithm
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Plotting graph for each sorting algorithm
def plot_sorting_performance():
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # Different array sizes
    quickSort_times = []
    mergeSort_times = []
    heapSort_times = []
    bubbleSort_times = []

    for size in sizes:
        arr = generate_random_array(size)

        # Time QuickSort
        arr_copy = arr.copy()
        quickSort_times.append(measure_time(quickSort, arr_copy))

        # Time MergeSort
        arr_copy = arr.copy()
        mergeSort_times.append(measure_time(mergeSort, arr_copy))

        # Time HeapSort
        arr_copy = arr.copy()
        heapSort_times.append(measure_time(heapSort, arr_copy))

        # Time BubbleSort
        arr_copy = arr.copy()
        bubbleSort_times.append(measure_time(bubbleSort, arr_copy))

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, quickSort_times, label="QuickSort", marker='o')
    plt.plot(sizes, mergeSort_times, label="MergeSort", marker='s')
    plt.plot(sizes, heapSort_times, label="HeapSort", marker='^')
    plt.plot(sizes, bubbleSort_times, label="BubbleSort", marker='x')

    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

# Calling the function to plot graph
plot_sorting_performance()
