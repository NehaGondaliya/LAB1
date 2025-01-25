def get_even_numbers(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    return [i for i in range(1, n + 1) if i % 2 == 0]

number = int(input("Enter the upper limit to find even numbers: "))
print(f"Even numbers between 1 and {number} are:")
print(get_even_numbers(number))
