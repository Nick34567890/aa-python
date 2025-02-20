import time
import matplotlib.pyplot as plt
import numpy as np

# Recursive Method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to measure execution time for the recursive method
def measure_time(fib_function, n):
    start_time = time.time()
    result = fib_function(n)
    end_time = time.time()
    return end_time - start_time, result

# First series of Fibonacci numbers (smaller values for the recursive method)
first_series = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37]

# Second series of Fibonacci numbers (larger values for comparison)
second_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

recursive_times_first_series = []
for n in first_series:
    recursive_time, _ = measure_time(fibonacci_recursive, n)
    recursive_times_first_series.append(recursive_time)

recursive_times_second_series = []
for n in second_series:
    recursive_time, _ = measure_time(fibonacci_recursive, n)
    recursive_times_second_series.append(recursive_time)

# Prepare data for plotting
x_values_first = first_series
y_values_first = recursive_times_first_series

x_values_second = second_series
y_values_second = recursive_times_second_series

# 1. Basic Line Graph
plt.figure(figsize=(10, 6))
plt.plot(x_values_first, y_values_first, label="Recursive Fibonacci Time (First Series)", color='b', marker='o')
plt.plot(x_values_second, y_values_second, label="Recursive Fibonacci Time (Second Series)", color='g', marker='x')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Recursive Fibonacci Function - Execution Time vs n')
plt.grid(True)
plt.legend()
plt.show()

# 2. Log-Scale Graph (To visualize exponential growth more clearly)
plt.figure(figsize=(10, 6))
plt.plot(x_values_first, y_values_first, label="Recursive Fibonacci Time (First Series)", color='b', marker='o')
plt.plot(x_values_second, y_values_second, label="Recursive Fibonacci Time (Second Series)", color='g', marker='x')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds, log scale)')
plt.title('Log-Scale: Recursive Fibonacci Function - Execution Time vs n')
plt.grid(True)
plt.legend()
plt.show()

