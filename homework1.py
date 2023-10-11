print("Hello world!")

######################################
# Problem 1:
x = 10
y = 2.5
# addition of 2 variables
sumOf = x + y
print("sum is : %d" % sumOf)
print("sum is : %2.2f" % sumOf)
# multiplication of 2 variables
productPf = x * y
print("multiplication is : %d" % productPf)
print("multiplication is : %2.2f" % productPf)
# subtraction of 2 variables
diff = x - y
print("subtraction is : %d" % diff)
print("subtraction is : %2.2f" % diff)
# division of 2 variables
div = x / y
print("division is : %d" % div)
print("division is : %2.2f" % div)
######################################
# Write a Python script that creates 5 string variables of 5 bulgarian PINs ( ЕГН ) and 5 names in
# tuples. Finally, insert only the pairs whose name begins with a vowel in a dictionary and print it.
egn = ("7305034321", "9910064536", "5103736893", "6302014789", "9010196754")
names = ("Metodi", "Simona", "Elena", "Neli", "Adelina")
# create a dictionary and zip key - egn with value-name
this_dict = dict(zip(egn, names))
# print initial dictionary
print("Initial dictionary:", this_dict)
# with list compression:
# keys = [k for k, v in this_dict.items() if v[0] == 'A' or v[0] == 'E' or v[0] == 'O' or v[0] == 'I' or v[0] == 'U']
# print("Filtered ", keys)
# create a new dictionary
newDict = dict()
for (key, value) in this_dict.items():
    if value[0] == 'A' or value[0] == 'E' or value[0] == 'O' or value[0] == 'I' or value[0] == 'U':
        newDict[key] = value

print("filtered dict:", newDict)

###################################################
# Problem 3:
# Fill in the following truth table. Use Python to verify the results.
# | x | y | x and y | x or y | not x | not y |
x = input("Enter your value: ")
y = input("Enter your value: ")
val = x and y
print("The result of x and y is", val)

x = input("Enter your value: ")
y = input("Enter your value: ")
val = x or y
print("The result of x or y is", val)

x = input("Enter your value: ")
val = not x
print("The result of not x is", val)

y = input("Enter your value: ")
val = not y
print("The result of not y is", val)
