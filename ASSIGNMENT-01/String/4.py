# Input strings
string1 = "dean"
string2 = "tom"

# Initialize an empty string to store the result
result = ""

# Iterate through characters in string1
for char in string1:
    # Check if the character exists in string2
    if char in string2:
        # Append the common character to the result
        result += char

# Check if there are common characters
if result:
    # Print the resulting string if there are common characters
    print(result)
else:
    # Print "Nothing in common" if there are no common characters
    print("Nothing in common")

