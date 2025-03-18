num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
    print(num1, "+", num2, "=", num1 + num2)
elif operation == '-':
    print(num1, "-", num2, "=", num1 - num2)
elif operation == '*':
    print(num1, "*", num2, "=", num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero. Please enter a nonzero number")
    else:
        print(num1 / num2)
else:
    print("Invalid operation")

