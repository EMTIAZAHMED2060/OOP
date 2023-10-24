class Customer:
    def __init__(self):
        self.tickets = []  
        self.total_price = 0
        self.max_tickets = 3  
        print("Welcome to ABC Memorial Park")

    def buyTicket(self, name, age):
        if len(self.tickets) < self.max_tickets:
            if age > 10:
                ticket_price = 100
            else:
                ticket_price = 50
            self.tickets.append((name, age, ticket_price))
            self.total_price += ticket_price
            print(f"Successfully purchased a ticket for {name}!")
        else:
            print("You can't buy more than 3 tickets")

    def showDetails(self):
       
        if len(self.tickets) > 0:
            
            print(f"Amount of tickets: {len(self.tickets)}")
            print(f"Total price: {self.total_price} Taka")
        else:
            print("No tickets purchased.")

# Driver code
print('1-------------------------')
customer1 = Customer()
print('2-------------------------')
customer1.buyTicket('Bob', 23)
customer1.buyTicket('Henry', 7)
customer1.buyTicket('Alexa', 30)
customer1.buyTicket('Jonas', 43)
print('3-------------------------')
customer1.showDetails()
print('4-------------------------')
customer2 = Customer()
print('5-------------------------')
customer2.buyTicket('Harry', 60)
customer2.buyTicket('Tomas', 28)
print('6-------------------------')
customer2.showDetails()

