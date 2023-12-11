class User:
    activities = ["Post", "Like", "Comment"]

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.activity_log = []

    def UserActivity(self, activityType):
        if activityType in User.activities:
            activity_message = f"{self.name} {activityType}d a post."
            self.activity_log.append(activity_message)
            print(activity_message)
        else:
            print("Invalid activity type.")

    def userDetails(self):
        user_details = f"Name: {self.name}\nEmail: {self.email}\nActivity Type: {self.activity_log}"
        return user_details


class BracbookUser(User):
    def __init__(self, name, email, phone="Not set"):
        super().__init__(name, email)
        self.phone = phone

# Testing the code
user1 = BracbookUser("Rakait", "xyz@gmail.com")
print("1===========================")
print(user1.userDetails())
print("2===========================")

user2 = BracbookUser("Sazzad", "abc@gmail.com", "01727xxxxxx")
print("3===========================")
print(user2.userDetails())
print("4===========================")

user1.UserActivity("Like")
print("5===========================")
user1.UserActivity("Comment")
print("6===========================")
print(user1.userDetails())
print("7===========================")

user2.UserActivity("Share")
print("8===========================")
user2.UserActivity("Comment")
print("9===========================")
print(user2.userDetails())
