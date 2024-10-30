 # Importing necessary libraries
import math 

# Define a class to represent a basic Calculator
class Calculator:
    def __init__(self):
        # Initialize calculator with basic operations
        self.result = 0

    # Method to add two numbers
    def add(self, x, y):
        """Adds two numbers and returns the result."""
        self.result = x + y
        return self.result
  
    # Method to subtract two numbers
    def subtract(self, x, y):
        """Subtracts the second number from the first and returns the result."""
        self.result = x - y
        return self.result

    # Method to multiply two numbers
    def multiply(self, x, y):
        """Multiplies two numbers and returns the result."""
        self.result = x * y
        return self.result

    # Method to divide two numbers
    def divide(self, x, y):
        """Divides the first number by the second and returns the result."""
        if y == 0:
            raise ValueError("Cannot divide by zero")  # Check for division by zero
        self.result = x / y
        return self.result

    # Method to calculate the square root of a number
    def square_root(self, x):
        """Returns the square root of a number."""
        if x < 0:
            raise ValueError("Cannot take the square root of a negative number")  # Check for negative input
        self.result = math.sqrt(x)
        return self.result

# Function to demonstrate the use of the Calculator class
def main():
    # Create an instance of the Calculator class
    calc = Calculator()

    # Perform addition
    add_result = calc.add(10, 5)
    print(f"Addition Result: {add_result}")

    # Perform subtraction
    subtract_result = calc.subtract(10, 5)
    print(f"Subtraction Result: {subtract_result}")

    # Perform multiplication
    multiply_result = calc.multiply(10, 5)
    print(f"Multiplication Result: {multiply_result}")

    # Perform division
    try:
        divide_result = calc.divide(10, 2)
        print(f"Division Result: {divide_result}")
    except ValueError as e:
        print(e)

    # Perform square root calculation
    try:
        sqrt_result = calc.square_root(16)
        print(f"Square Root Result: {sqrt_result}")
    except ValueError as e:
        print(e)

# Entry point of the program
if __name__ == "__main__":
    main()
