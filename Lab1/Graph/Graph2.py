import time
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Dynamic Programming Method (Iterative version)
def fibonacci_dynamic_programming_iterative(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Function to measure execution time for the dynamic programming method
def measure_time(fib_function, n):
    start_time = time.time()
    result = fib_function(n)
    end_time = time.time()
    return end_time - start_time, result

# Second series of Fibonacci numbers (larger values for comparison)
second_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Create the PrettyTable object
table = PrettyTable()

# Set the column names
table.field_names = ["n / Time (s)", *second_series]

# Add the row for dynamic programming times
dp_times = []
for n in second_series:
    dp_time, _ = measure_time(fibonacci_dynamic_programming_iterative, n)
    dp_times.append(f"{dp_time:.6f}")

# Add row data to the table
table.add_row(["DP Time (s)", *dp_times])

# Collect the DP times for plotting
dp_times = []
for n in second_series:
    dp_time, _ = measure_time(fibonacci_dynamic_programming_iterative, n)
    dp_times.append(dp_time)

# Prepare data for plotting
x_values = second_series
y_values = dp_times

# 1. Basic Line Graph
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="DP Fibonacci Time", color='b', marker='o')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Dynamic Programming Fibonacci Function - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 2. Log-Scale Graph
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="DP Fibonacci Time", color='r', marker='x')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds, log scale)')
plt.title('Log-Scale: Dynamic Programming Fibonacci - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 3. Scatter Plot Graph
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, color='g', label='Execution Time')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Scatter Plot: DP Fibonacci - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 4. Bar Graph
plt.figure(figsize=(10, 6))
plt.bar(x_values, y_values, color='m')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Bar Graph: DP Fibonacci - Execution Time vs n (Second Series)')
plt.grid(True)
plt.show()

# Print the table
print(table)
