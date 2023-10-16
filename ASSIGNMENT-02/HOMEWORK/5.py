def key_generator(*names):
    encrypted_keys = []

    for name in names:
        first_char = name[0].lower()
        last_char = name[-1].upper()
        middle_chars = name[1:-1][::-1]  
        ascii_values = [str(ord(char)) for char in middle_chars] 
        middle_chars = ''.join(ascii_values)  

        encrypted_key = f"{first_char}{middle_chars}{last_char}"
        encrypted_keys.append(encrypted_key)

    return encrypted_keys

employee_names = ["Alex", "Bob", "Trudy"]
encrypted_keys = key_generator(*employee_names)

print("Encrypted Keys:", encrypted_keys)
