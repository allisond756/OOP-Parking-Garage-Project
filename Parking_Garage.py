class ParkingGarage():
    """
        Attributes:
        - tickets --> list
        - parkingSpaces --> list
        - currentTicket --> dictionary
    """
    
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    # takeTicket() should decrease the amount of tickets by 1. It should also decrease the 
    # amount of parking spaces by 1.

    def takeTicket(self, oneTicket = 1, oneParkingSpot = 1):
        if len(self.tickets) == 4:
            print('\nThere are no available parking spaces at the moment')
        else:
            self.tickets.append(oneTicket)
            self.parkingSpaces.append(oneParkingSpot)
            print('\nPlease take your ticket for your parking spot')

    # payForParking() should display an input that waits for user to enter amount and stores it
    # to a variable . If variable is empty display message to pay for ticket. If not empty 
    # display message to user that ticket is paid and have 15 mins to exit garage. This should
    # update currentTicket dict key "paid" to True

    def payForParking(self, currentTicket = None):
        if currentTicket == None:
            currentTicket = self.currentTicket
            ticket_payment = input('\nPlease pay $5 for your parking ticket')
            if ticket_payment == str(""):
                print('\nNo payment has been made for parking ticket. Please pay $5 for your ticket')
            else:
                currentTicket["paid"] = True
                print('\nThank you for your payment, you have 15 minutes to exit the parking garage')

    # leaveGarage() if ticket has been paid display a thank you message. If ticket has not been
    # paid display a message to prompt payment (once paid display thank you message). Should
    # update parkingSpaces list to increase by 1 and ticket list increase by 1.

    def leaveGarage(self, currentTicket = None, oneTicket = 1, oneParkingSpot = 1):
        if currentTicket is None:
            currentTicket = self.currentTicket
        if currentTicket["paid"] == False:
            print('\nNo payment has been made for parking ticket. Please pay $5 for your ticket')
            ticket_payment = input('\nPlease pay $5 for your parking ticket')
            if ticket_payment == str(""):
                print('\nNo payment has been made for parking ticket. Please pay $5 for your ticket')
            else:
                currentTicket["paid"] = True
                print('\nThank you for your payment, have a nice day!')
        else:
            print('\nThank you, have a nice day!')


    # runGarage() will run the parkingGarage() class

parkingLotA = ParkingGarage([], [], currentTicket = {"paid": False})

def runGarage():
    while True:
        response = input('\nWhat would you like to do? \nTake Ticket?\nPay for Parking? \nLeave Garage?')

        if response.lower() == 'take ticket':
            parkingLotA.takeTicket()
        elif response.lower() == 'pay for parking':
            parkingLotA.payForParking()
        elif response.lower() == 'leave garage':
            parkingLotA.leaveGarage()
        else:
            print('\nTry another action')

runGarage()

    





        
        