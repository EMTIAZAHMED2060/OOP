class Mobile:
    countryCodes = {"880": "Bangladesh", "966": "India", "455": "USA"}

    def __init__(self, model, simCardStatus):
        self.model = model
        self._simCardStatus = simCardStatus  # Change to protected attribute
        self.balance = 0
        self.dialCallHistory = []
        print(f"Model {model} is manufactured.")

    def setSimCardStatus(self, status):
        self._simCardStatus = status
        print("SIM card status updated successfully.")

    def getSimCardStatus(self):
        return self._simCardStatus

    def rechargeSIMCard(self, amount):
        self.balance += amount
        print(f"Recharge successful! Current balance {self.balance} TK.")

    def dialCall(self, phoneNumber):
        # Extract the country code from the phone number
        country_code = phoneNumber[:3]

        # Check SIM card status
        if not self._simCardStatus:  # Access the protected attribute
            print("No SIM card available!")
            return

        # Check if dialing is allowed in the region
        if country_code not in self.countryCodes:
            print(f"Dialing is not allowed in this region.")
            return

        # Check for sufficient balance
        if self.balance <= 0:
            print("Insufficient balance!")
            return

        # Make the call
        print(f"Dialing the number {phoneNumber} to {self.countryCodes[country_code]} region.")
        self.dialCallHistory.append(phoneNumber)

class Nokia(Mobile):
    def __init__(self, model, simCardStatus, initial_balance=0):
        super().__init__(model, simCardStatus)
        self.balance = initial_balance

    def changeSIMCardStatus(self):
        super().setSimCardStatus(not super().getSimCardStatus())  # Call the base class method
        print("SIM card status updated successfully.")

# Driver code
N3110 = Nokia("N3110", False)
print("#######################################")
print(N3110)
print("1======================================")

N1100 = Nokia("N1100", True, 100)
print("#######################################")
print(N1100)
print("2======================================")

print(N3110.dialCall("88017196xxxx"))
print("3======================================")

N3110.changeSIMCardStatus()
print("4======================================")

print(N3110.dialCall("88017196xxxx"))
print("5======================================")

N3110.rechargeSIMCard(200)
print("6======================================")

print(N3110.dialCall("88017196xxxx"))
print("7======================================")

print(N1100.dialCall("45617196xxxx"))
print("8======================================")

print(N1100.dialCall("45517196xxxx"))
print(N1100.dialCall("96617196xxxx"))
print("9======================================")

print(f"Dial call history for {N1100.model}:\n{N1100.dialCallHistory}")
print(f"Dial call history for {N3110.model}:\n{N3110.dialCallHistory}")
