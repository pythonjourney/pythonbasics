input_string = input()

# Initialize the vowel count to 0
vowel_count = 0

# Define the set of vowels
vowels = "aeiou"

# Initialize the index
index = 0

# Loop through the string using a while loop
while index < len(input_string):
    # Check if the current character is a vowel
    if input_string[index] in vowels:
        vowel_count += 1
    # Move to the next character
    index += 1
    
print(vowel_count)


#logic here !
# input_string = input()
# i = 0
# while i < len(input_string):
#     # your condition to check if input_string[i] is a vowel
#     i += 1