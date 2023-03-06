class ParkingGarage:
    def __init__(self):
        self.tickets = 100
        self.parkingSpaces = 50
        self.currentTicket = {"ticket_number": None, "paid": False}
    
    def takeTicket(self):
        if self.tickets > 0 and self.parkingSpaces > 0:
            self.tickets -= 1
            self.parkingSpaces -= 1
            self.currentTicket["ticket_number"] = self.tickets + 1
            print(f"Please take your ticket. Your ticket number is {self.currentTicket['ticket_number']}.")
        elif self.tickets == 0:
            print("Sorry, the garage is full. Please come back later.")
        elif self.parkingSpaces == 0:
            print("Sorry, the garage is closed. Please come back during business hours.")
    
    def payForParking(self):
        payment = input("Please enter your payment amount: ")
        if payment != "":
            self.currentTicket["paid"] = True
            print("Your ticket has been paid. You have 15 minutes to leave.")
        else:
            print("Payment not received. Please pay for your ticket.")
    
    def leaveGarage(self):
        if self.currentTicket["paid"] and input()== "leave":
            print("Thank you for your visit. Have a nice day!")
            self.parkingSpaces += 1
            self.tickets += 1
            self.currentTicket = {"ticket_number": None, "paid": False}
        else:
            self.payForParking()


garage = ParkingGarage()

garage.takeTicket()
garage.payForParking()
garage.leaveGarage()
