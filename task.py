# Input handling: Get user input for their name and three favorite numbers
name = input("Enter your name: ")
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))

# Print statement and f-Strings: Greet the user
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Lists: Store the numbers in a list
numbers = [num1, num2, num3]

# Tuples: Store even/odd information in tuples within a list
even_odd_info = []
for num in numbers:
    if num % 2 == 0:  # Operators: Check if the number is even
        even_odd_info.append((num, "even"))
    else:
        even_odd_info.append((num, "odd"))

# For loop: Iterate over the list and print whether each number is even or odd
for num, info in even_odd_info:
    print(f"The number {num} is {info}.")

# For loop and Tuples: Create and print a tuple with each number and its square
for num in numbers:
    square_tuple = (num, num ** 2)  # Operators: Calculate the square
    print(f"The number {num} and its square: {square_tuple}")

# Operators: Calculate the sum of the numbers
total_sum = num1 + num2 + num3
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

# Prime number check using a simple for loop and conditions
is_prime = True
if total_sum <= 1:
    is_prime = False
else:
    for i in range(2, total_sum):
        if total_sum % i == 0:
            is_prime = False
            break

# Print statement and f-Strings: Notify the user if the sum is prime
if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")
