from sympy import python

def add(x, y):
    """
    Adds two numbers together.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts the second number from the first number.

    Args:
        x (int or float): The number from which to subtract.
        y (int or float): The number to subtract.

    Returns:
        int or float: The result of the subtraction.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers together.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The product of the two numbers.
    """
    return x * y

def divide(x, y):
    """
    Divides two numbers and returns the result.

    Parameters:
    x (float): The numerator.
    y (float): The denominator.

    Returns:
    float: The result of the division if y is not zero.
    str: An error message if y is zero.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y

def percentage(x, y):
    """
    Calculate the percentage of x with respect to y.

    Args:
        x (float): The part value.
        y (float): The total value.

    Returns:
        float: The percentage value of x with respect to y.

    Raises:
        ZeroDivisionError: If y is zero.
    """
    return (x / y) * 100

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

    try:
        choice = input("Enter choice(1/2/3/4/5): ")
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == '5':
        print(f"{num1} is {percentage(num1, num2)}% of {num2}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()