print("SIMPLE CALCULATOR..!")
print("Type 1 for addition")
print("Type 2 for subtraction")
print("Type 3 for multiplication")
print("Type 4 for division")
print("Type 5 to exit the program...!!")

a = int(input("Select between 1/2/3/4/5: "))

if a == 5:
    print("Closing the program, goodbye!")

elif a == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 + num2)

elif a == 2:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 - num2)

elif a == 3:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 * num2)

elif a == 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid input. Please choose between 1 to 5.")
