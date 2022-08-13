from car import Car
from electricCar import ElectricCar

honda_car = Car('Honda', 'Accord', '2011')
print(honda_car.get_fuel_level())
honda_car.fill_tank()
print(honda_car)

tesla_car = ElectricCar('Tesla', 'Model S', '2018')
print(tesla_car.get_charge_level())
tesla_car.charge_battery()
print(tesla_car)

#overwrite
tesla_car.fill_tank()
tesla_car.get_fuel_level()