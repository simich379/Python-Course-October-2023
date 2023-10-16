import random

###############################################################
# Problem 0: Write a program that takes an integer input from the user and checks if it's odd or even. Use an if-else
# statement to print the result
# ##############################################################

number = int(input("Please enter a numer:"))

if number % 2 == 0:
    print("The number is even")
else:
    print("the number is odd")

# ##############################################################
# Problem 1:
# Write a Python program to find the sum of all even numbers from 1 to 100 using a loop. Make
# use of control flow constructs like the for loop and conditional statements.
# ##############################################################
sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum += i
print("Sum is :", sum)

# ##############################################################
# Write a Python script that prompts the user in the console a simple problem ( how much does 5
# + 17 equal to ) until the user provides a correct answer.

result = int(input("How much does 5 + 17 equal to "))

while True:

    if result == 22:
        print("The answer is correct! ")
        break
    else:
        print("Please enter new answer")
        result = int(input("Input a number : "))

print("The result is", result)

# ##############################################################
# Problem 3:
# Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is
# divisible by 3, "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5.


for number in range(1000):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("Iteration:", number)
        pass
print("Loop finished")

# ##############################################################
# Problem 4:
# Design a Python program that simulates a simple guessing game. The program should generate
# a random number between 1 and 100 and ask the user to guess it. Provide hints like "Too high"
# or "Too low" until the user guesses the correct number. Use a while loop for this game


random_number = random.randint(1, 100)
print(random_number)

while True:
    mysteriousNumber = int(input("Input a number : "))
    if mysteriousNumber > 100:
        print("Out of range!")
    elif mysteriousNumber == random_number:
        print("Bingo!")
        break
    elif mysteriousNumber > random_number:
        print("Too high!")
    elif mysteriousNumber < random_number:
        print("Too low!")
    else:
        print("Continue")

# ##############################################################
# TODO
# Problem 5:
# Modify problem 2 so that every time the user is prompted the problem is different. Think of a
# way to design that and come up with a proper solution for that.
#
firstNumber = int(input("Enter a value for the first number : "))
secondNumber = int(input("Enter a value for the second number : "))
operation = input("Choose operation: +,-,*,/,% : ")

while True:

    match operation:
        case "+":
            result = firstNumber + secondNumber
            print("The result is :", result)
            break
        case "-":
            if firstNumber > secondNumber:
                result = firstNumber - secondNumber
            else:
                result = secondNumber - firstNumber
            print("The result is :", result)
            break
        case "*":
            result = firstNumber * secondNumber
            print("The result is :", result)
            break

        case "/":
            result = firstNumber / secondNumber
            print("The result is :", result)
            break

        case "%":
            result = firstNumber % secondNumber
            print("The result is :", result)
            break
        case _:
            print("Enter a valid operator")
            break


# # ##############################################################
# Problem 6:
# Write a Python program that takes an integer input from the user and prints the multiplication
# table for that number from 1 to 10 using a for loop.

multiplication_table_number = int(input("Enter a number :"))
multiplication_table = 0;
if multiplication_table_number < 0:
    print("Enter a positive number.")
    multiplication_table_number = int(input("Enter a number :"))

else:
    for i in range(1, 11):
        multiplication_table = multiplication_table_number * i
        print(f"{multiplication_table_number} * {i} = {multiplication_table}")

# ###############################################################
# Problem 7:
# Create a Python program that checks if a given integer is a prime number. Use a for loop to
# iterate through possible divisors and use an if-else statement to determine if it's prime.

prime_number = int(input("Enter a number :"))
size = (prime_number / 2) + 1
if prime_number > 1:
    for num in range(2, int(size)):
        if (prime_number % num) == 0:
            print(prime_number, "is not a prime number")
            break
        else:
            print(prime_number, "is a prime number")
else:
    print(prime_number, "is not a prime number")

# ##############################################################

# Problem 8: Pattern Printing
# Write a program that takes an integer 'n' as input and prints the following pattern using nested
# for loops:
# Expected output for input 5:
# 1
# 12
# 123
# 1234
# 12345
size_of_n = int(input("Input a number called n : "))

for i in range(1, size_of_n + 1):
    for j in range(1, i+1):
        # end is print function param; By default, the value of this parameter is ‘\n’
        print(j, end='')
    print('')


