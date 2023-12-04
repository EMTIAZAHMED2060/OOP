class Passenger:
    count = 0
    base_fare = 450
    extra_charge_21_50 = 50
    extra_charge_above_50 = 100
    weight_allowance = 20

    def __init__(self, name):
        self.name = name
        self.bag_weight = 0
        Passenger.count += 1

    def set_bag_weight(self, weight):
        self.bag_weight = weight

    def calculate_fare(self):
        fare = Passenger.base_fare

        if self.bag_weight > Passenger.weight_allowance:
            excess_weight = self.bag_weight - Passenger.weight_allowance

            if excess_weight <= 30:
                fare += Passenger.extra_charge_21_50
            else:
                fare += Passenger.extra_charge_above_50

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
