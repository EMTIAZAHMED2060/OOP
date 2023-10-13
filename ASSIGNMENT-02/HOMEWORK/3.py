def assign_students_to_sections(sections, *student_names):
    section_dict = {section: [] for section in sections}

    for name in student_names:
        ascii_sum = sum(ord(char) for char in name)
        section_index = ascii_sum % len(sections)
        section = sections[section_index]
        section_dict[section].append(name)

    return section_dict

sections = 'ABCDE'
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
result = assign_students_to_sections(sections, *students)
print(result)
