class Spaceship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_cargo_weight = 0
        self.cargo = []

    def load_cargo(self, cargo):
        cargo_weight = cargo.get_weight()
        available_capacity = self.capacity - self.current_cargo_weight

        if available_capacity >= cargo_weight:
            # There is enough space for the cargo
            self.cargo.append(cargo.get_name())
            self.current_cargo_weight += cargo_weight
        else:
            # Not enough space for the cargo
            excess_weight = cargo_weight - available_capacity
            print(f"Warning: Unable to load {cargo.get_name()} inside {self.name}. "
                  f"Exceeds capacity by {excess_weight}.")

    def display_details(self):
        print(f"Spaceship Name: {self.name}")
        print(f"Capacity: {self.capacity}")
        print(f"Current Cargo Weight: {self.current_cargo_weight}")
        print(f"Cargo: {self.cargo}")
        

class Cargo:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight


# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()

