s = input("Please enter a string:")

idx1 = -1
idx2 = -1

# Find the position of the first uppercase letter
for i in range(len(s)):
    if ord('A') <= ord(s[i]) <= ord('Z'):
        idx1 = i
        break

# Find the position of the last uppercase letter
for i in range(len(s) - 1, -1, -1):
    if ord('A') <= ord(s[i]) <= ord('Z'):
        idx2 = i
        break

# Check if both uppercase letters were found
if idx1 != -1 and idx2 != -1:
    result = s[idx1 + 1:idx2]
    print(result)
else:
    print("BLANK")
