import time
import matplotlib.pyplot as plt
import numpy as np

# Optimized Fibonacci using Iteration (no recursion depth issue)
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Function to measure execution time for the iterative method
def measure_time(fib_function, n):
    start_time = time.time()
    result = fib_function(n)
    end_time = time.time()
    return end_time - start_time, result

# Second series of Fibonacci numbers (larger values for comparison)
second_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Collect the iterative times for the second series
iterative_times_second_series = []
for n in second_series:
    iterative_time, _ = measure_time(fibonacci_iterative, n)
    iterative_times_second_series.append(iterative_time)

# Prepare data for plotting
x_values_second = second_series
y_values_second = iterative_times_second_series

# 1. Basic Line Graph
plt.figure(figsize=(10, 6))
plt.plot(x_values_second, y_values_second, label="Iterative Fibonacci Time (Second Series)", color='g', marker='x')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Iterative Fibonacci Function - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 2. Log-Scale Graph (To visualize exponential growth more clearly)
plt.figure(figsize=(10, 6))
plt.plot(x_values_second, y_values_second, label="Iterative Fibonacci Time (Second Series)", color='g', marker='x')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds, log scale)')
plt.title('Log-Scale: Iterative Fibonacci Function - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 3. Scatter Plot Graph
plt.figure(figsize=(10, 6))
plt.scatter(x_values_second, y_values_second, color='g', label='Second Series Execution Time')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Scatter Plot: Iterative Fibonacci Function - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 4. Bar Graph (to show the comparison of execution times for each n)
plt.figure(figsize=(10, 6))
plt.bar(x_values_second, y_values_second, color='g')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Bar Graph: Iterative Fibonacci Function - Execution Time vs n (Second Series)')
plt.grid(True)
plt.show()
