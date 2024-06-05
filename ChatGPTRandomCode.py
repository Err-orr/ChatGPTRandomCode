import random

random_number = random.randint(1, 100)
print("Random number:", random_number)

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Calculate the average of the random numbers
average = sum(random_numbers) / len(random_numbers)

print("Random Numbers:", random_numbers)
print("Average:", average)

def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Generate the first 10 numbers in the Fibonacci sequence
result = fibonacci(10)
print(result)
