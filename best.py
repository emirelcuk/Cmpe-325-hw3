 # Importing necessary libraries
import math 

# Define a class to represent a basic Calculator
class Calculator:

   

@app.route('/commit_history/<int:commit_id>')
def commit_details(commit_id):
    user = session.get("user")
    
    # Commit verisini ID ile alıyoruz
    commit = Commit.query.get(commit_id)

    if commit:
        # Commit ile ilişkili SonarQube verilerini alıyoruz
        issues_list = commit.issues_list  # Commit'e ait issues listesi
        measures_data = commit.measures_data  # Commit'e ait measures verisi

        # Commit'in detaylarını commit_details.html gibi bir template'e gönderiyoruz
        return render_template(
            'commit_details.html',
            commit=commit,
            user=user,
            issues_list=issues_list,
            measures_data=measures_data
        )

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
