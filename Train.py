seats = 80 * 6
extra_seats = 80 * 8

class Train:
    def __init__(self):
        self.journey_foot_top = {9: {"seats": seats, "Total_income": 0, "passengers": 0},
                                 11: {"seats": seats, "Total_income": 0, "passengers": 0},
                                 13: {"seats": seats, "Total_income": 0, "passengers": 0},
                                 15: {"seats": seats, "Total_income": 0, "passengers": 0}}
        self.journey_top_foot = {10: {"seats": seats, "Total_income": 0, "passengers": 0},
                                 12: {"seats": seats, "Total_income": 0, "passengers": 0},
                                 14: {"seats": seats, "Total_income": 0, "passengers": 0},
                                 16: {"seats": extra_seats, "Total_income": 0, "passengers": 0}}
        self.cost = 25

    def train_time(self):

        print("\tFOOT TO TOP")
        print("Time of Train\tAvailable Seats")
        for train_timing in self.journey_foot_top:
            print(f"{train_timing}\t\t\t\t {self.journey_foot_top[train_timing]['seats']}")
        print("\tTOP TO FOOT")
        for train_timing in self.journey_top_foot:
            print(f"{train_timing}\t\t\t\t {self.journey_top_foot[train_timing]['seats']}")

    def book_seat(self, booking_seats, departure_time, return_time):
        if self.journey_foot_top[departure_time]['seats'] >= booking_seats:
            if self.journey_top_foot[return_time]['seats'] >= booking_seats:
                free_ticket = int(booking_seats / 10)
                #foot to top
                self.journey_foot_top[departure_time]['seats'] -= booking_seats
                self.journey_foot_top[departure_time]['passengers'] += booking_seats
                self.journey_foot_top[departure_time]['Total_income'] += (booking_seats-free_ticket)*self.cost
                #top top foot
                self.journey_top_foot[return_time]['seats'] -= booking_seats
                self.journey_top_foot[return_time]['passengers'] += booking_seats
                self.journey_top_foot[return_time]['Total_income'] += (booking_seats - free_ticket) * self.cost
                #setting close
                if self.journey_foot_top[departure_time]['seats'] == 0:
                    self.journey_foot_top[departure_time]['seats'] = "closed"
                if self.journey_top_foot[return_time]['seats'] == 0:
                    self.journey_top_foot[return_time]['seats'] = "closed"
                return True

    def customer_bill(self, booking_seats):
        free_ticket = int(booking_seats / 10)
        if free_ticket > 0:
            print(f"You got {free_ticket*self.cost} discount!")
        customer_bill = (booking_seats-free_ticket) * self.cost
        print(f"Your Total bill is:{customer_bill}")

    def train_history(self):
        print("\tFOOT TO TOP")
        print("TimeofTrain\tTotalSeatsBooked\tTotalIncome")
        for train_timing in self.journey_foot_top:
            print(f"{train_timing}\t\t\t\t {self.journey_foot_top[train_timing]['passengers']}\t\t\t\t{self.journey_foot_top[train_timing]['Total_income']}")
        print("\tTOP TO FOOT")
        for train_timing in self.journey_top_foot:
            print(f"{train_timing}\t\t\t\t {self.journey_top_foot[train_timing]['passengers']}\t\t\t\t{self.journey_top_foot[train_timing]['Total_income']}")



