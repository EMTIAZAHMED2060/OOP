class Train:
    def __init__(self, name, *args):
        self.name = name
        self.args = args
        print(f'Welcome aboard on {name}\nStart: {args[0]}\nDestination: {args[-1]}')
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            print(f'{passenger.pname} welcome aboard')
            if passenger.start is None:
                passenger.start = self.args[0]
            if passenger.d is None:
                passenger.d = self.args[-1]
            self.passengers.append(passenger)

    def all_passenger_details(self):
        for passenger in self.passengers:
            print(f'Name: {passenger.pname},', end='')
            print(f'Start: {passenger.start}, Destination: {passenger.d},', end='')
            idx1 = 0
            idx2 = 0
            for j in range(len(self.args)):
                if passenger.start == self.args[j]:
                    idx1 = j
                if passenger.d == self.args[j]:
                    idx2 = j
            passenger.fare = (idx2 - idx1) * 100
            print(f'Fare: ${passenger.fare}')


class Passenger:
    def __init__(self, name, start=None, d=None):
        self.pname = name
        self.start = start
        self.d = d
        self.fare = None


t1 = Train('T1-Express', 'New York', 'Manhattan', 'Brooklyn', 'Boston')
print("1========================")
p1 = Passenger("Naruto")
t1.add_passenger(p1)
p2 = Passenger("Sasuke", "Manhattan")
p3 = Passenger("Hinata", "Manhattan", "Brooklyn")
print("2========================")
t1.add_passenger(p2, p3)
print("3========================")
t1.all_passenger_details()
print("4========================")
t2 = Train('Europe-Express', 'London', 'Paris', 'Brussels', 'Turkey')
print("5========================")
p4 = Passenger("Max", "London", "Brussels")
p5 = Passenger("Eleven", "Paris")
p6 = Passenger("Mike", "Brussels")
t2.add_passenger(p4, p5, p6)
print("6========================")
t2.all_passenger_details()
