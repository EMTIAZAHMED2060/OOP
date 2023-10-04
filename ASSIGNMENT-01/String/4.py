# Input strings
string1 = "harry"
string2 = "hermione"

# Initialize an empty string to store the result
result = ""

# Iterate through characters in string1
for char in string1:
    # Check if the character exists in string2
    if char in string2:
        # Append the common character to the result
        result += char

# Print the resulting string
print(result)
