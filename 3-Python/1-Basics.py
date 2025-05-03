import math
from datetime import date

print("Welcome to the Python world!")

# String
print('Single Quotation String')
print("Double Quotation String")
print('''Triple Quotation(\''') String
    This is a multi-line string.''')	
print("""Triple Quotation(\""") String
This is a multi-line string.\n""")	

# Variable
name = "Sayem"
age = 24
print("My name is", name, "and I am", age, "years old.")
print(f"f-string (String Interpolation): My name is {name} and I am {age} years old.") # f-string (String Interpolation)
print("format method (String Interpolation): My name is {} and I am {} years old.\n".format(name, age)) # format method (String Interpolation)

# () => Parentheses
# [] => Square Brackets
# {} => Curly Braces
print("() => Parentheses\n[] => Square Brackets\n{} => Curly Braces\n")

# Data Types
print("Data Types")
print("String:", type(name))
print("Integer:", type(age))
print("Float:", type(3.14)) # Float (Decimal)
print("Boolean:", type(2 == 2), "\n") # Boolean (True/False)

# Arithmetic Operators
print("Add:", 3+2)
print("Sub:", 3-2)
print("Mul:", 3*2)
print("Div:", 3/2)
print("Floor Div:", 3//2)
print("Pow:", 3**2) # Exponentiation
print("Mod:", 3%2, "\n") # Modulus

# Comparison Operators
print("Equal:", 3==2)
print("Not Equal:", 3!=2)
print("Greater Than:", 3>2)
print("Less Than:", 3<2)
print("Greater Than or Equal To:", 3>=2)
print("Less Than or Equal To:", 3<=2, "\n")

# Logical Operators
              # True       False
print("And:", (2 < 3) and (3 > 4))
print("Or:", (2 < 3) or (3 > 4))
print("Not:", not True, "\n") 

# List (Array): [element1, element2, element3]	
fruits = ["Apple", "Banana", "Orange"]

# in operator (Membership Operator)
print("Hello" in "HelloWorld") 
print("hello" in "HelloWorld")
print(2 in [1, 2, 3], "\n")	


# input 
name = input("Enter your name: ")
print("Hello,", name, "\n")	


num1 = int(input("Enter first number: ")) # input() returns a string, so we need to convert it to int
num2 = int(input("Enter second number: ")) # So, we use type casting to convert it to int
print("Sum:", num1 + num2)
print("Floor: ", math.floor(num1 / num2)) # Floor Division
print("Ceil: ", math.ceil(num1 / num2)) # Ceil Division
print("Square Root:", math.sqrt(num1)) # Square Root
print("Power:", math.pow(num1, num2)) # Power
print("Max:", max(num1, num2)) # Maximum
print("Min:", min(num1, num2)) # Minimum
print("Absolute:", abs(num1)) # Absolute Value
print("Round:", round(num1 / num2)) # Round
print("Pi:", math.pi) # Pi Value

print("Today is:", date.today()) # Date