# calculator.py

# 1. Use functions for each operation
def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers, with a check for division by zero"""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def main():
    """Main function to run the calculator loop"""
    
    # 3. Loop until user chooses to exit
    while True:
        # Display menu
        print("\n--- Simple Command-Line Calculator ---")
        print("Select operation:")
        print("  +  (Add)")
        print("  -  (Subtract)")
        print("  * (Multiply)")
        print("  /  (Divide)")
        print("  q  (Quit)")

        # 2. Take user input
        choice = input("Enter choice (+, -, *, /, or q): ")

        # Check if the user wants to quit
        if choice == 'q':
            print("Exiting calculator. Goodbye!")
            break

        # Check if the choice is a valid operation
        if choice in ('+', '-', '*', '/'):
            try:
                # Get numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle non-numeric input
                print("Invalid input. Please enter numbers only.")
                continue # Skip to the next loop iteration

            # Perform calculation based on choice
            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)
            
            # Print the result
            print(f"Result: {result}")

        else:
            # Handle invalid operation choice
            print("Invalid choice. Please select one of the options.")

# Standard Python entry point
if __name__ == "__main__":
    main()