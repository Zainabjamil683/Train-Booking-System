from Train import Train
train = Train()
print("Welcome to train")
print("Start your Bookings")
day_start = True
while day_start:
    train.train_time()
    no_of_seats = int(input("Enter the number of seats you want to book: "))
    departure_time = int(input("Enter the departure time: "))
    return_time = int(input("Enter thr return time: "))
    if train.book_seat(no_of_seats, departure_time, return_time):
        print("Thankyou for booking our train!")
        train.customer_bill(no_of_seats)
    else:
        print("Seats not available! Please look into the table of available seats.")
    day_end = input("Is the day end? If yes then close booking otherwise continue bookings? ")
    if day_end == "yes":
        day_start = False

print("Train Full Day History")
train.train_history()

