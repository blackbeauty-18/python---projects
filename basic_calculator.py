num1 = float(input("Enter first number: "))
op = input("Enter valid operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("This is an addition operation, Your answer is: ")
    print(num1 + num2)
elif op == "-":
    print("This is a subtraction operation, Your answer is:")
    print(num1 - num2)
elif op == "*":
    print("This is a multiplication operation, Your answer is:")
    print(num1 * num2)
elif op == "/":
    print("This is a division operation, Your answer is:")
    print(num1 / num2)
elif op == "//":
    print("This is a floor operation, Your answer is:")
    print(num1 // num2)
elif op == "%":
    print("This is a modulus , Your answer is:")
    print(num1 % num2)
else:
    print("Invalid operator, Try again!")