class Car():
    """Representing a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.fuel_tank_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        print('Filling fuel tank to the fullest...')
        self.fuel_level = self.fuel_tank_capacity

    def get_fuel_level(self):
        print('Getting fuel level for you...')
        return self.fuel_level

    def __str__(self):
        return "{} {} {} Fuel Level = {}\n".format(self.make, self.model, self.year, self.fuel_level)
