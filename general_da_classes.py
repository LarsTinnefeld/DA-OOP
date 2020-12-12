class Combat_unit():
    def __init__(self, armor, speed, weight, energy_consumption, charge_level = 100):
        self.armor = armor
        self.speed = speed
        self.weight = weight
        self.energy_consumption = energy_consumption
        self.charge_level = charge_level

    def charging(self):
        self.charge_level = 100

    def discharge(self):
        self.charge_level -= self.energy_consumption

        if self.charge_level <=0:
            self.charge_level = 0
            print("Charge Level is zero")



