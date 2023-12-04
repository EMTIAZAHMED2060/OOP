class BracuStudent:
    def __init__(self, student_name, home_location):
        self.student_name = student_name
        self.home_location = home_location
        self.has_bus_pass = False

    def show_details(self):
        print(f"Student Name: {self.student_name}\nHome Location: {self.home_location}")
        print(f"Has Bus Pass? {self.has_bus_pass}")

    def acquire_bus_pass(self):
        self.has_bus_pass = True


class BracuBus:
    def __init__(self, bus_route, max_capacity=2):
        self.bus_route = bus_route
        self.max_capacity = max_capacity
        self.passenger_list = []
        self.passenger_count = 0

    def show_details(self):
        print(f"Bus Route: {self.bus_route}\nPassenger Count: {self.passenger_count} (Max: {self.max_capacity})")
        print(f"Passengers on Board: {self.passenger_list}")

    def board_students(self, *students):
        if not students:
            print("No passengers!")
        else:
            for student in students:
                if not student.has_bus_pass:
                    print(f"{student.student_name}, you don't have a bus pass!")
                else:
                    if student.home_location != self.bus_route:
                        print(f"{student.student_name}, you boarded the wrong bus!")
                    else:
                        if self.passenger_count < self.max_capacity:
                            print(f"{student.student_name} boarded the bus.")
                            self.passenger_list.append(student.student_name)
                            self.passenger_count += 1
                        else:
                            print("Bus is full!")


# Driver Code
student1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
student2 = BracuStudent("Shanto", "Motijheel")
student3 = BracuStudent("Taskin", "Mirpur")
student1.show_details()
student2.show_details()
print("2===========================")
student3.show_details()
print("3===========================")
bus_mirpur = BracuBus("Mirpur")
bus_azimpur = BracuBus("Azimpur", 5)
bus_mirpur.show_details()
bus_azimpur.show_details()
print("4===========================")
student2.acquire_bus_pass()
student3.acquire_bus_pass()
print("5===========================")
student2.show_details()
student3.show_details()
print("6===========================")
bus_mirpur.board_students()
print("7===========================")
bus_mirpur.board_students(student1, student2)
print("8===========================")
student1.acquire_bus_pass()
student2.home_location = "Mirpur"
student1.show_details()
student2.show_details()
print("9===========================")
bus_mirpur.board_students(student1, student2, student3)
print("10===========================")
bus_mirpur.show_details()
