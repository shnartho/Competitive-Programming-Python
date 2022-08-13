class Battery:
    """Representing a car battery"""
    def __init__(self, size):
        self.battery_size = size
        self.charge_level = 0

    def charge_battery_full(self):
        print('Charging the battery for you...')
        self.charge_level = self.battery_size

    def get_charge_level(self):
        return self.charge_level
