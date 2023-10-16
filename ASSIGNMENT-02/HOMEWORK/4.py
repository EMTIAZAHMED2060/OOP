def username_generator(first_name, last_name, student_id, middle_name=""):
    first_part = first_name[:3].upper()
    if middle_name:
        middle_part = middle_name
    else:
        middle_part = ""
    
    last_part = last_name[-3:].lower()
    id_part = str(student_id)[-4:]
    
    username = f"{first_part}{middle_part}{last_part}_{id_part}"
    return username

first_name = input("First Name: ")
middle_name = input("Middle Name: ")
last_name = input("Last Name: ")
student_id = (input("Student ID:"))

print(username_generator(first_name, last_name, student_id))
