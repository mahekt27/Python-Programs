# Function with arguments and parameters: multiplication and division

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Multiplication of", num1, "and", num2, "=", multiply(num1, num2))
print("Division of", num1, "by", num2, "=", divide(num1, num2))