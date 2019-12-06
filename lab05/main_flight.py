from flight import Flight

flight1 = Flight(10, 'Tirana', 'Roma', 100)
flight2 = Flight(20, 'Roma', 'Ankara', 110)
flight3 = Flight(10, 'Tirana', 'Bari', 90)

flights = (flight1, flight2, flight3)


def show_flights():
    for flight in flights:
        flight.to_string()
        print('-'*20)


show_flights()

flight1.reserve(15)
flight2.reserve(10)
flight3.reserve(10)

print('After reservation:')
print()

show_flights()

flight2.cancel(10)
flight3.cancel(15)  # note that we are cancelling more than we reserved

flight1.set_destination('Berlin')
flight2.set_source('Amsterdam')
flight1.set_seats(70)

print('After cancellation:')
print()

show_flights()

print('Flight 1 == Flight 2:', flight1.equal(flight2))
print('Flight 2 == Flight 3:', flight2.equal(flight3))
print('Flight 3 == Flight 1:', flight3.equal(flight1))
