# Sample input passwords
passwords = ["ohMyBR@CU", "ohmybracu", "OhMyBR@CU20"]

for password in passwords:
    lowercase_missing = True
    uppercase_missing = True
    digit_missing = True
    special_missing = True

    # Check for lowercase letters
    for c in password:
        if 'a' <= c <= 'z':
            lowercase_missing = False
            break

    # Check for uppercase letters
    for c in password:
        if 'A' <= c <= 'Z':
            uppercase_missing = False
            break

    # Check for digits
    for c in password:
        if '0' <= c <= '9':
            digit_missing = False
            break

    # Check for special characters
    for c in password:
        if c in "_,$,#,@":
            special_missing = False
            break

    if lowercase_missing:
        print("Lowercase missing")
    if uppercase_missing:
        print("Uppercase missing")
    if digit_missing:
        print("Digit missing")
    if special_missing:
        print("Special character missing")

    if not (lowercase_missing or uppercase_missing or digit_missing or special_missing):
        print("OK")
