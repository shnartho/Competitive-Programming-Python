from car import Car
from battery import Battery

class ElectricCar(Car):
    """Representing an electric car"""

    def __init__(self, make, model, year):
        super().__init__(make,model,year)

        self.battery = Battery(70)

    def charge_battery(self):
        self.battery.charge_battery_full()

    def get_charge_level(self):
        return self.battery.get_charge_level()

    def fill_tank(self):
        print("Electric car doesn't have fuel tank")

    def get_fuel_level(self):
        print("Electric car doesn't have fuel tank")

    def __str__(self):
        return "{} {} {} Charge Level = {}\n".format(self.make, self.model, self.year,self.battery.charge_level)
