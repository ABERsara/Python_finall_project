from flight_ticket import FlightTicket
from flight import Flight, FlightSystem
from payment import Payment
from datetime import date, datetime
import calendar
# instance of flight system
flightSys = FlightSystem()
def createTickets(flight, places):
    """Create tickets for the passengers"""
    for i in range(places):
        name = input(f"Insert the name of passenger num {i + 1}")
        passport = input(f"Insert the passport number of passenger num {i + 1}")
        # Call the get_next_seat method to get the next seat number
        seat = flight.get_next_seat()
        ticket = FlightTicket(flight, name, passport, seat)
        ticket.printCard()
def get_valid_expiration_date():
    """Allows only valid date """
    while True:
        try:
            month = int(input("Insert the credit validity month (1-12): "))
            if 1 <= month <= 12:
                break
            else:
                print("Error, the month must be a number between 1-12.")
        except ValueError:
            print("Error, please enter a valid number for the month.")

    while True:
        try:
            year = int(input("Insert the credit validity year: "))
            current_year = datetime.now().year
            if current_year <= year <= current_year + 10:  # Assume cards are valid for the next 10 years
                break
            else:
                print(f"Error, the year must be between {current_year} and {current_year + 10}.")
        except ValueError:
            print("Error, please enter a valid number for the year.")

    return month, year
def choosePlaces():
    """Get the customer to choose how many places he want on the flight"""
    while True:
        try:
            places = int(input("Insert how many places you want on the flight:"))
            break  # This breaks out of the inner loop, not the outer one
        except:
            print("The item you inserted is illegal, try again")
    return places
def payCreditCard():
    """Take the details of the credit card from the client, returns if pay is done"""
    creditNum = input("Insert the credit number")
    threeDigits = input("Insert the credit three digits")
    expiration_month, expiration_year = get_valid_expiration_date()
    validity = date(expiration_year, expiration_month, 1)
    IDofCardHolder = input("Insert the ID of the card holder")
    secretCod = input("Insert the credit secretCod")
    if Payment(creditNum, threeDigits, validity, IDofCardHolder, secretCod).payCard(currentFlight.price * places):
        return True
    else:
        return False
def chooseFlightDate():
    """Choose a date from the calendar for the desired flight"""
    while True:
        cal = calendar.month(2024, 1)
        print(f"Here is the calendar for the next month:\n{cal}")
        try:
            day = int(input("choose The day you want to fly from the calendar:"))
            flightList = flightSys.findFlights(date(2024, 1, day), cityCode)
            if flightList:
                flights = [Flight(flight.flightNum, flight.targetCity, flight.airCode, flight.date, flight.numPlaces,
                              flight.price, flight.airline) for flight in flightList]
                for flight in flights:
                    flight.printFlight()
                return flights
            else:
                print("Sorry, we have no flights to offer you on this date. Please try another day.")
                return None
        except:
            print("You enter an illegal format for a day. insert a number of day.")

#########################################################################
# turn on the travel agency
on = True
while on:
    # The customer chooses a destination
    dest = input("Hello and welcome to the travel agency Airland! What is your desired destination?")
    cityCode = flightSys.findCityCode(dest)
    if cityCode != None:
        # choose a date for a flight
        flights=chooseFlightDate()
        #  choose a flight
        chooseFlight = False
        while not chooseFlight:
            flightNum=input("Insert the desired flight number ")
            if flights:
                for flight in flights:
                    if flight.flightNum==flightNum:
                        places = choosePlaces()
                        if not flight.Availability(places):
                            print("Sorry, but there are not enough places on this flight, please insert another flight ")
                        else:
                            chooseFlight = True
                            currentFlight = flight
                            break  # This breaks out of the outer loop
            # print the flight details
            currentFlight.printFlight()
        # receives  the credit details for payment
        pay=False
        while not payCreditCard():
                print("The credit did not go through, enter another number or try again")
        createTickets(currentFlight, places)
    else:
        print("Sorry, we have no flights to offer you at this destination. Please try another one.")
    stop=input("Do you want torn off? press yes or not")
    if stop=="yes":
        on = False
