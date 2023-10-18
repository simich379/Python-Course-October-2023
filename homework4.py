import geometry


# ##############################################################
# Problem 0:
# Complete the following function so that it returns the sum of the elements in the list passed as
# an argument


def sum_elements(array=None):
    if array is None:
        array = []
    result = 0
    for item in range(len(array)):
        result += array[item]
    return result


print(sum_elements([1, 2, 3, 4]))
print(sum_elements([0]))
print(sum_elements([]))
print(sum_elements([-1, 1]))


# ##############################################################
# Problem 1: Simple Calculator Function
# Define a function called `simple_calculator` that takes two numbers and an operator ('+', '-', '*',
# or '/') as arguments and returns the result of the operation.

def simple_calculator(num1=0, num2=0, operator='+'):
    num1 = int(input("Enter a first number : "))
    num2 = int(input("Enter a second number : "))
    operator = input("Enter a operator - +,-.*,/,% : ")
    result = 0
    match operator:
        case "+":
            result = num1 + num2

        case "-":
            result = num1 - num2

        case "*":
            result = num1 * num2

        case "/":
            result = num1 / num2

        case "%":
            result = num1 % num2
    return result


print(simple_calculator())

# ##############################################################
# Problem 2: Area of Shapes
# Create a module named `geometry` with functions to calculate the area of common shapes like
# a square, rectangle, triangle, and circle. Import this module and use it to calculate the areas of
# different shapes.

print("Triangle Function")
breadth = float(input("Enter a value for the breadth : "))
height = float(input("Enter a value for the height : "))
print("Area of the Triangle is : ", geometry.AreaOfTriangle(breadth, height))

print("Square Function")
side = float(input("Enter a value for the side of square : "))
print("Area of the Square is :", geometry.AreaOfSquare(side))

print("Rectangle Function")
breadth = float(input("Enter a value for the breadth : "))
height = float(input("Enter a value for the length : "))
print("Area of the Rectangle is : ", geometry.AreaOfRectangle(breadth, height))

print("Circle Function")
radius = float(input("Enter a value for the radius : "))
print("Area of the Rectangle is : ", geometry.AreaOfCircle(radius))


# ##############################################################
# Problem 3: Temperature Conversion
# Write a program that converts temperatures between Celsius and Fahrenheit. Create two
# functions, one for each conversion, and use them in a program to convert temperatures
# provided by the user

# Formula : Fahrenheit Temperature = (1.8 * celsius) + 32;
def fromCelsiusesFahrenheit(temperature):
    return (1.8 * temperature) + 32


def fromFahrenheitToCelsiuses(temperature):
    return (temperature - 32) / 1.8


temperatuteCel = int(input("Input a Celsiuses temperature : "))
print("Temperature from Celsiuses to Fahrenheit is : ", fromCelsiusesFahrenheit(temperatuteCel), "°F")
temperatuteFahr = int(input("Input a Fahrenheit temperature : "))
print("Temperature from Celsiuses to Fahrenheit is : ", fromFahrenheitToCelsiuses(temperatuteFahr), "°C")

# ##############################################################
# Problem 4: Online Shopping Cart
# Create a Python program that simulates an online shopping cart using a global dictionary
# variable. Every customer has unique id as a key. Define functions to add items to the cart,
# remove items, calculate the total price, and display the contents of the cart. Allow the user to
# interact with the cart by adding and removing items.

print(globals())

shopping_cart = {}


def add_items():
    item = input(" What would you like to add?  ")
    price = float(input(" type in the price "))
    shopping_cart[item] = price
    print(f"'{item}' has  added item to his/her cart.")
    print(f" The price is {price}")
    return shopping_cart


def remove_items(remove_item=None):
    if remove_item is None:
        remove_item = {}
    remove_item = input(" Type in what you would like to remove?  ")
    shopping_cart.pop(remove_item)
    return shopping_cart


def calculate_total_price():
    total = 0
    for item in shopping_cart:
        total += shopping_cart[item]
    print(f" The total price in the shopping cart is {total}")


def display_the_contents():
    print("This is what is in your shopping cart")
    for item in shopping_cart:
        print(f"  {item} - {shopping_cart[item]}")


add_items()
add_items()
add_items()
display_the_contents()
remove_items()
calculate_total_price()
display_the_contents()
# ##############################################################
