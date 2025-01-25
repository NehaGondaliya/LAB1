def generate_fibonacci(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

number = int(input("Enter the number of Fibonacci terms to generate: "))
print(f"The first {number} terms of the Fibonacci sequence are:")
print(generate_fibonacci(number))
