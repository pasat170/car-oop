import json

from car import Car
from client import Client
from rental import Rental
from system import CarSystem


def quick_client_status(cl):
    print(f"{cl.name} has rented {len(cl.cars)} cars.")
    print(f"{cl.name} balance: {cl.money}\n")


with open('cars.json') as json_cars:
    cars = json.load(json_cars)

system = CarSystem([Car.from_dict(car) for car in cars])
system.list_available_cars()

# client_1
Hristo = Client('Hristo', 8000)
Hristo_rental1 = Rental('CB7628BA', hours=8, days=2)
Hristo_rental2 = Rental('A2277TA', weeks=2)
Hristo_rental3 = Rental('CT7777TT', days=1)
Hristo_rental4 = Rental('A2277TA', hours=5, days=3)
system.rent([Hristo_rental1, Hristo_rental2, Hristo_rental3, Hristo_rental4], Hristo)
quick_client_status(Hristo)

# client_2
Ivan = Client('Ivan', 5000)
Ivan_rental1 = Rental('PB2924TC', hours=10)
Ivan_rental2 = Rental('PB6797KM', days=8)
Ivan_rental3 = Rental('PB7781HA', weeks=2)
Ivan_rental4 = Rental('PB3407HH', hours=6)
system.rent(
    [Ivan_rental1, Ivan_rental2, Ivan_rental3, Ivan_rental4],
    Ivan
)
quick_client_status(Ivan)
