# Problem 44: Print Fibonacci sequence
# Find and fix the error

def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
