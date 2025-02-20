import time
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt

# Matrix multiplication function
def matrix_mult(A, B):
    return np.dot(A, B)

# Matrix exponentiation function
def matrix_pow(M, power):
    result = np.array([[1, 0], [0, 1]])  # Identity matrix
    base = M

    while power > 0:
        if power % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power //= 2

    return result

# Function to compute the nth Fibonacci number using matrix exponentiation
def fibonacci_matrix_power(n):
    if n <= 1:
        return n

    F = np.array([[1, 1], [1, 0]])  # Matrix for Fibonacci numbers
    result_matrix = matrix_pow(F, n - 1)
    return result_matrix[0][0]

# Function to measure execution time for the matrix power method
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

# Add the row for matrix power method times
matrix_times = []
for n in second_series:
    matrix_time, _ = measure_time(fibonacci_matrix_power, n)
    matrix_times.append(f"{matrix_time:.6f}")

# Add row data to the table
table.add_row(["Matrix Power Time (s)", *matrix_times])

# Collect the Matrix Power times for plotting
matrix_times = []
for n in second_series:
    matrix_time, _ = measure_time(fibonacci_matrix_power, n)
    matrix_times.append(matrix_time)

# Prepare data for plotting
x_values = second_series
y_values = matrix_times

# 1. Basic Line Graph
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Matrix Power Fibonacci Time", color='b', marker='o')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Matrix Power Fibonacci Function - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 2. Log-Scale Graph
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Matrix Power Fibonacci Time", color='r', marker='x')
plt.xscale('linear')
plt.yscale('log')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds, log scale)')
plt.title('Log-Scale: Matrix Power Fibonacci - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 3. Scatter Plot Graph
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, color='g', label='Execution Time')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Scatter Plot: Matrix Power Fibonacci - Execution Time vs n (Second Series)')
plt.grid(True)
plt.legend()
plt.show()

# 4. Bar Graph
plt.figure(figsize=(10, 6))
plt.bar(x_values, y_values, color='m')
plt.xlabel('n (Fibonacci term)')
plt.ylabel('Execution Time (seconds)')
plt.title('Bar Graph: Matrix Power Fibonacci - Execution Time vs n (Second Series)')
plt.grid(True)
plt.show()

# Print the table
print(table)
