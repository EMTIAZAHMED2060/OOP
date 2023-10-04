# Take input as a string
input_string = input("Enter a string: ")


is_number = True
is_word = True

for char in input_string:
    if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
        is_word = False
    if not ('0' <= char <= '9'):
        is_number = False


if is_number:
    print("NUMBER")
elif is_word:
    print("WORD")
else:
    print("MIXED")