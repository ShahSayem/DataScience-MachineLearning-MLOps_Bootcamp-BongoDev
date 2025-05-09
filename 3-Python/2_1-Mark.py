# Logical / Conditional statements
# if, elif, else
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("You will get job placement Option")
elif marks >= 60:
    print("You will get the certificate")
elif marks < 40:
    print("Failed")
else:
    print("No certificate!!!")