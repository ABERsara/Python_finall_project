from flight import Flight

class FlightTicket(Flight):

    def __init__(self, flight, name, passport, seat):
        super().__init__(flightNum=flight.flightNum, targetCity=flight.targetCity, airCode=flight.airCode,
                         date=flight.date, numPlaces=flight.numPlaces, price=flight.price, airline=flight.airline)
        self.name = name
        self.passport = passport
        self.seat = seat

    def printCard(self):
        """Print the card's details for the user"""
        filename = f"ticket{self.flightNum}{self.passport}.txt"

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(f"name: {self.name}\npassport number: {self.passport}\nnumber flight: {self.flightNum}\n"
                       f"airport code: {self.airCode}\ndate: {self.date}\nseat: {self.seat}\n\n"
                       f" ✈️ {self.airline} wish you to have a good flight! ✈️ ")

        with open(filename, mode="r", encoding="utf-8") as file:
            print(file.read())
