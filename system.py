from rental import Rental

class CarSystem:
    def __init__(self, cars):
        print("Initializing car system")
        self.cars = cars
        self.rented_cars = []

    def list_available_cars(self):
        print("Available cars to rent")
        print('\n', '\n'.join(
            [str(car) for car in self.cars if car not in self.rented_cars]
        ), '\n')

    def rent(self, rentals, client):
        if isinstance(rentals, Rental):
            rentals = [rentals]
        
        available_cars = self.get_available_cars(rentals)
        if available_cars:
            total_cost = self.calculate_total_cost(rentals, available_cars)

            if total_cost > client.money:
                print(f"{client.name} doesn't have enough money to pay!")
                return
            
            print("Rented car/s:", '\n', '\n'.join(map(str, available_cars)))
            print(f"Total cost: {total_cost}")
            client.add_cars(*available_cars)
            client.change_balance(-total_cost)
            self.rented_cars.extend(available_cars)

    def get_available_cars(self, rentals):
        available_cars = []
        for car_id in [rental.car_id for rental in rentals]:
            car = next((car for car in self.cars if car.id == car_id), None) 
            if not car:
                print(f"{car_id} car doesn't exist!")
                return

            if car in self.rented_cars:
                print(f"{car_id} has been rented already!")
                continue

            available_cars.append(car)

        return available_cars

    @staticmethod
    def calculate_total_cost(rentals, available_cars):
        total_cost = 0

        for car in available_cars:
            rental = next(rental for rental in rentals if rental.car_id == car.id)
            total_cost += (rental.hours * car.cost_per_hour) + \
                          (rental.days * car.cost_per_day) + \
                          (rental.weeks * car.cost_per_week)

        if len(available_cars) > 3:
            # Apply sale discount
            print("-30% discount applied!")
            total_cost = 0.7 * total_cost

        return total_cost
