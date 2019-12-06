def short_and_capital(name):
    name = name.upper()

    if len(name) > 3:
        name = name[:3]

    return name


class Flight:
    def __init__(self, number, source, destination, seats):
        self.number = number
        self.source = short_and_capital(source)
        self.destination = short_and_capital(destination)
        self.total_seats = seats  # cannot be changed (considered as immutable)
        self.available_seats = seats  # can be changed through reserving and cancelling

    def get_number(self):
        return self.number

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    # The getter and setter for seats refer to available_seats
    # total_seats is considered immutable, much like (flight) number
    # which doesn't have a setter (hence "immutable")
    def get_seats(self):
        return self.available_seats

    def set_source(self, source):
        self.source = short_and_capital(source)

    def set_destination(self, destination):
        self.destination = short_and_capital(destination)

    def set_seats(self, seats):
        self.available_seats = seats

        # Makes sure that we don't end up with more seats
        # than we started with (when cancelling reservations)
        if self.available_seats > self.total_seats:
            self.available_seats = self.total_seats

    def reserve(self, seats):
        if self.available_seats < seats:
            print("Not enough seats. Can't reserve.")
        else:
            self.available_seats -= seats

    def cancel(self, seats):
        self.set_seats(self.available_seats + seats)

    def equal(self, other):
        return self.number == other.number

    def to_string(self):
        print('Flight No:', self.number)
        print('From:', self.source)
        print('To:', self.destination)
        print('Total seats:', self.total_seats)
        print('Available seats:', self.available_seats)
