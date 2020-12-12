from general_da_classes import Combat_unit

class Ground_vehicle(Combat_unit):
    
    def __init__(self, armor, speed, weight, energy_consumption, charge_level, vehicle_type):

        Combat_unit.__init__(self, armor, speed, weight, energy_consumption, charge_level)
        self.vehicle_type = vehicle_type

    def ramming(self, damage):

        self.armor -= damage * 0.5
        print("Caused damage: {}".format(damage))