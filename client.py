class Client:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cars = []

    def add_cars(self, *cars):
        self.cars.extend(cars)

    def change_balance(self, amount):
        self.money += amount
