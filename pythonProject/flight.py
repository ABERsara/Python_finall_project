from datetime import date, datetime

class Flight:
    def __init__(self, flightNum, targetCity, airCode, date, numPlaces, price, airline):
        self.flightNum = flightNum
        self.exit = "Israel"
        self.targetCity = targetCity
        self.airCode = airCode
        self.date = date
        self.numPlaces = numPlaces
        self.price = price
        self.airline = airline
        self.numPassengers = 0
        self.seat_generator = self.updateSeat()

    def printFlight(self):
        """Print the flight's details"""
        print(f"Flight details:\n\tflight number: {self.flightNum}\n\tairport code: {self.airCode}\n\tairline: {self.airline}\n\t"
              f"date: {self.date}\n\tprice: {self.price}")

    def Availability(self, numSeats):
        """Check (and return) if there is available places on the desired flight"""
        return self.numPlaces >= self.numPassengers + numSeats

    def updateSeat(self):
        """Update the number of seat as the number of current passengers """
        for seat in range(1, self.numPlaces + 1):
            self.numPassengers += 1
            yield seat

    def get_next_seat(self):
        """Get the next seat available"""
        return next(self.seat_generator)

class FlightSystem:
    """Initializes the flight system's data in a dictionary,
    the key is the target of flight and the values- dictionaries of key:
     flight's date and values: instances of flights"""
    def __init__(self):
        self.flightSystem={
            "PAR":{
                date(2024,1,1):
                    [Flight(flightNum="1672934673",targetCity="Paris",airCode="CDG",date= datetime(2024,1,1,22,10),numPlaces=50,price=1000,airline="EL AL"),
                     Flight(flightNum="1672934673",targetCity="Paris",airCode="CDG",date= datetime(2024,1,1,7,30),numPlaces=50,price=1000,airline="AIR FRANCE")],
                date(2024, 1, 5):
                    [Flight(flightNum="1672934673",targetCity="Paris",airCode="CDG",date= datetime(2024,1,5,8,40),numPlaces=50,price=1000,airline="DELTA" )],
                date(2024, 1, 20):
                    [Flight(flightNum="1672934673", targetCity="Paris",airCode="CDG",date= datetime(2024,1,20,13,50),numPlaces=50,price=1000,airline="")],

            },
            "ZRH":{

            },
            "GVA":{

            },
            "NYC":{

            },
            "LON":{

            },
            "VIE":{

            },
            "MIL":{

            },
            "WAW":{

            },
            "PRG":{

            },
            "LAX":{

            }
        }
        self.cityCode={
            "Paris":"PAR",
            "Zurich":"ZRH",
            "Geneva":"GVA",
            "New York":"NYC",
            "London":"LON",
            "Vienna":"VIE",
            "Milan":"MIL",
            "Warsaw":"WAW",
            "Prague":"PRG",
            "Los Angeles":"LAX"
        }

    def findCityCode(self,city):
            """Find the city cod"""
            # Check if the city exists on list,append it to the list
            cities=[fCity for fCity in self.cityCode.keys() if fCity==city]
            if cities:
                return self.cityCode[city]
            return None

    def findFlights(self,date,cityCode):
            """Find a list of all the flights on this day"""
            # Check if the date exists on list, append it to the list
            dates=[fdate for fdate in self.flightSystem[cityCode].keys() if fdate==date]
            if dates:
                flightList=[flight for flight in self.flightSystem[cityCode][date]]
                return flightList
            return None
