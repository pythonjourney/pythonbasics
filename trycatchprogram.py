def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of dividing {a} by {b} is {result}.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:

# Normal division
divide_numbers(10, 2)

# Division by zero
divide_numbers(10, 0)

# Invalid data types
divide_numbers(10, "five")

