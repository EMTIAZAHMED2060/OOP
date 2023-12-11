class Passenger:
    count = 0
    bf = 450
    ext21 = 50
    ecb50 = 100
    wa = 20

    def __init__(self, name):
        self.name = name
        self.bw = 0
        Passenger.count += 1

    def set_bag_weight(self, weight):
        self.bag_weight = weight

    def calculate_fare(self):
        fare = Passenger.bf

        if self.bw > Passenger.wa:
            excess_weight = self.bw - Passenger.wa

            if excess_weight <= 30:
                fare += Passenger.ext21
            else:
                fare += Passenger.ecb50

        return fare

    def printDetail(self):
        print("Name:", self.name)
        print("Bus Fare:", self.calculate_fare(), "taka")
        print("=========================")

# Test the code
print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)
