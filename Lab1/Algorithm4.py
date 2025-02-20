import time
import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from decimal import Decimal, getcontext

getcontext().prec = 1000  # Arbitrary precision (set to a higher value)

def fibonacci_binet(n):
    """
    Computes the nth Fibonacci number using Binet's formula.
    """
    phi = Decimal(1 + math.sqrt(5)) / Decimal(2)
    fib_n = (phi**n - (-phi)**(-n)) / Decimal(math.sqrt(5))
    return round(fib_n)

def measure_time(fib_function, n):
    """
    Measures the execution time of a Fibonacci function.
    """
    start_time = time.time()
    result = fib_function(n)
    end_time = time.time()
    return end_time - start_time, result

def display_fibonacci_table(series):
    """
    Displays a table of Fibonacci numbers with their computation times in a horizontal format.
    """
    table = PrettyTable()

    # Field names will be based on the Fibonacci terms
    table.field_names = ["Metric"] + [f"n={n}" for n in series]

    # Prepare the data rows
    fib_numbers = []
    times = []

    for n in series:
        fib_time, fib_number = measure_time(fibonacci_binet, n)
        fib_numbers.append(f"{fib_number:,}")  # Display the Fibonacci numbers with commas for readability
        # Format time with 3 decimal places, like 0.000999
        times.append(f"{fib_time:.3f}")

    # Add the rows for Fibonacci numbers and time
    table.add_row(["Fibonacci(n)", *fib_numbers])
    table.add_row(["Time (seconds)", *times])

    # Print the table
    print(table)

# Plotting the performance of the Binet method
def plot_execution_times(series):
    """
    Plots the execution time of the Fibonacci Binet method.
    """
    x_values = series
    y_values = []

    for n in series:
        binet_time, _ = measure_time(fibonacci_binet, n)
        y_values.append(binet_time)

    # 1. Basic Line Graph
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="Binet Fibonacci Time", color='b', marker='o')
    plt.xlabel('n (Fibonacci term)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Binet Fibonacci Function - Execution Time vs n')
    plt.grid(True)
    plt.legend()
    plt.show()

    # 2. Log-Scale Graph
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="Binet Fibonacci Time", color='r', marker='x')
    plt.xscale('linear')
    plt.yscale('log')
    plt.xlabel('n (Fibonacci term)')
    plt.ylabel('Execution Time (seconds, log scale)')
    plt.title('Log-Scale: Binet Fibonacci - Execution Time vs n')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
try:
    n_values = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
    display_fibonacci_table(n_values)  # Display Fibonacci numbers with time
    plot_execution_times(n_values)    # Plot the execution times
except ValueError as ve:
    print(ve)