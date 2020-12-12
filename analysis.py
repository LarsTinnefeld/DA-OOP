from general_da_classes import Combat_unit

class Ground_vehicle(Combat_unit):
    
    def __init__(self, armor, speed, weight, energy_consumption, charge_level, vehicle_type):

        Combat_unit.__init__(self, armor, speed, weight, energy_consumption, charge_level)
        self.vehicle_type = vehicle_type

    def ramming(self, damage):

        self.armor -= damage * 0.5
        print("Caused damage: {}".format(damage))


    def __repr__(self):

        return "This is a combat unit of the type {}.\nProperties\nArmor: {}\nSpeed: {}\nWeight: {}\nEngery consumption: {}\n\nIt's current charge level is {}.".format(self.vehicle_type, self.armor, self.speed, self.weight, self.energy_consumption, self.charge_level)