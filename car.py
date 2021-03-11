class Car:
    def __init__(
        self, id, brand, model, consumption,
        cost_per_hour, cost_per_day, cost_per_week
    ):
        self.id = id
        self.brand = brand
        self.model = model
        self.consumption = consumption
        self.cost_per_hour = cost_per_hour
        self.cost_per_day = cost_per_day
        self.cost_per_week = cost_per_week

    @classmethod
    def from_dict(cls, dict):
        return cls(
            dict['id'], dict['brand'], dict['model'],
            dict['consumption'], dict['cost_per_hour'],
            dict['cost_per_day'], dict['cost_per_week']
        )

    def __repr__(self):
        return self.id
