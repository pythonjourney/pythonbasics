a, b = map(int, input().split())
c = a + b
print(c)


# input().split()
# input() reads a line of input from the user as a string.
# .split() splits the input string into a list of substrings based on whitespace. For example, if the user inputs "3 4", input().split() will return ['3', '4'].
# map()
# map() is a built-in Python function that applies a given function to all items in an input list (or any iterable) and returns a map object (which can be converted to a list, tuple, etc.).
# The first argument to map() is the function to be applied (in this case, int), and the second argument is the iterable (in this case, the list of substrings from input().split()).
# int
# int is a built-in Python function that converts a string (or another number type) to an integer.
# When you use map(int, input().split()), you are doing the following:

# input().split() takes the user's input and splits it into a list of strings. For example, if the user inputs "3 4", this results in ['3', '4'].
# map(int, ['3', '4']) applies the int function to each item in the list, converting each string to an integer. This results in a map object containing [3, 4].
# Here’s an example to illustrate this:

# python
# Copy code
# # Example input: "3 4"
# user_input = "3 4"  # Simulating user input
# split_input = user_input.split()  # Split the input into a list of strings
# print(split_input)  # Output: ['3', '4']

# mapped_input = map(int, split_input)  # Apply int() to each item in the list
# mapped_list = list(mapped_input)  # Convert the map object to a list
# print(mapped_list)  # Output: [3, 4]

# a, b = mapped_list  # Unpack the list into variables a and b
# c = a + b  # Add the integers
# print(c)  # Output: 7
# In the one-liner a, b = map(int, input().split()), the map object is directly unpacked into the variables a and b. This is a concise way to convert the input strings to integers and assign them to variables in one step.