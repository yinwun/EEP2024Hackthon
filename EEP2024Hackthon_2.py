def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b."""
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

def main():
    """Main function to perform arithmetic operations."""
    num1 = 10
    num2 = 5

    sum_result = add(num1, num2)
    difference = subtract(num1, num2)
    product = multiply(num1, num2)
    quotient = divide(num1, num2)

    print(f"Addition: {num1} + {num2} = {sum_result}")
    print(f"Subtraction: {num1} - {num2} = {difference}")
    print(f"Multiplication: {num1} * {num2} = {product}")
    print(f"Division: {num1} / {num2} = {quotient}")

if __name__ == "__main__":
    main()
