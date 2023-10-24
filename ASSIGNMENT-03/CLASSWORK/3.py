class GreenPhone:
    def __init__(self, model_name, android_version, num_cameras):
        self.phone_company = "GreenPhone"
        self.model_name = model_name
        self.android_version = android_version
        self.num_cameras = num_cameras

    def showSpecification(self):
        print(f"Phone Company: {self.phone_company}")
        print(f"Model Name: {self.model_name}")
        print(f"Android Version: {self.android_version}")
        print(f"Number of Cameras: {self.num_cameras}")

    def updatePhone(self):
        if self.android_version < 15:
            self.android_version += 1
            print(f"Your phone {self.phone_company} {self.model_name} is upgraded to Android Version: {self.android_version}.")
        else:
            print(f"Your phone {self.phone_company} {self.model_name} is already up to date.")

# Driver code
print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()
