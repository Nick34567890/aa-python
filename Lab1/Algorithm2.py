import time
from prettytable import PrettyTable

# Dynamic Programming Method with Memoization
def fibonacci_dynamic_programming(n, memo={}):
    # If the result is already in the memo dictionary, return it
    if n in memo:
        return memo[n]

    # Base cases
    if n <= 1:
        return n

    # Recursively compute the Fibonacci number with memoization
    memo[n] = fibonacci_dynamic_programming(n - 1, memo) + fibonacci_dynamic_programming(n - 2, memo)
    return memo[n]

# Function to measure execution time for the dynamic programming method
def measure_time(fib_function, n):
    start_time = time.time()
    result = fib_function(n)
    end_time = time.time()
    return end_time - start_time, result

# First series of Fibonacci numbers (smaller values for the dynamic programming method)
first_series = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42]
# Change to second and see the result \/
# second_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Create the PrettyTable object
table = PrettyTable()

# Set the column names
table.field_names = ["n / Time (s)", *first_series]

# Add the row for dynamic programming times
dp_times = []
for n in first_series:
    dp_time, _ = measure_time(fibonacci_dynamic_programming, n)
    dp_times.append(f"{dp_time:.6f}")

# Add row data to the table
table.add_row(["DP Time (s)", *dp_times])
import matplotlib.pyplot as plt

# Collect the DP times
dp_times = []
for n in first_series:
    dp_time, _ = measure_time(fibonacci_dynamic_programming, n)
    dp_times.append(dp_time)

# Prepare data for plotting
x_values = first_series
y_values = dp_times

# 1. Basic Line Graph
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="DP Fibonacci Time", color='b', marker='o')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Dynamic Programming Fibonacci Function - Execution Time vs n')
plt.grid(True)
plt.legend()
plt.show()





# Print the table
print(table)
