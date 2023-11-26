class BracuStudent:
    def __init__(self, student_name, home_location):
        self.student_name = student_name
        self.home_location = home_location
        self.has_bus_pass = False

    def show_details(self):
        print(f"Student Name: {self.student_name}\nLives in {self.home_location}")
        print(f"Has Bus Pass? {self.has_bus_pass}")

    def get_bus_pass(self):
        self.has_bus_pass = True


class BracuBus:
    def __init__(self, bus_route, max_capacity=2):
        self.bus_route = bus_route
        self.max_capacity = max_capacity
        self.passenger_list = []
        self.passenger_count = 0

    def show_details(self):
        print(f"Bus Route: {self.bus_route}\nPassengers Count: {self.passenger_count} (Max: {self.max_capacity})")
        print(f"Passengers on Board: {self.passenger_list}")

    def board(self, *students):
        if not students:
            print("No passengers!")
        else:
            for student in students:
                if not student.has_bus_pass:
                    print(f"{student.student_name}, you don't have a bus pass!")
                else:
                    if student.home_location is not self.bus_route:
                        print(f"{student.student_name}, you got on the wrong bus!")
                    else:
                        if self.passenger_count < self.max_capacity:
                            print(f"{student.student_name} boarded the bus.")
                            self.passenger_list.append(student.student_name)
                            self.passenger_count += 1
                        else:
                            print("Bus is full!")


# Driver Code
st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_bus_pass()
st3.get_bus_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_bus_pass()
st2.home_location = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
