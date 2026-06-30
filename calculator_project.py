import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
#TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

n1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
n2 = int(input("Enter second number: "))

result = operations[operator](n1, n2)
print(result)
print("\n")
should_continue = input("Do you want to continue with this result or start a new calculation? Type yes or no.\n")

while should_continue == "yes":
    n1 = result
    operator = input("Enter operator (+, -, *, /): ")
    n2 = int(input("Enter second number: "))
    print(operations[operator](n1, n2))

else:
    print("\n" * 100)
    n1 = int(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    n2 = int(input("Enter second number: "))
    print(operations[operator](n1, n2))