import math

class Gtp_module():
    ''' The GTP_module class represents a pick environment of an automated pick process according the goods to picker principle.

        Inputs:
        - required order lines per hour
        - required required units_per_hour

        Outputs:
        - Sizing in required GTP units
        - Investment price in Euros
        - FTE requirement in FTEs per shift
    '''

    def __init__(self, req_units_per_hour, req_lines_per_hour):
        self.req_units_per_hour = req_units_per_hour
        self.req_lines_per_hour = req_lines_per_hour

        # Following are module-specific constants
        self.cost_per_unit = 500000 # Euros per station
        self.capacity_per_unit = 600 # order lines per picker (station)

    def sizer(self):
        ''' The sizer is calculating the required amount of units to fulfill the needed capacity.
        
        Inputs: None

        Outputs: Amount of needed GTP units
        '''
        self.module_cluster_size = math.ceil(self.req_lines_per_hour / self.capacity_per_unit)
        return self.module_cluster_size

    def update_module_capacity(self):
        '''Updates the module specific capacity'''

        self.capacity_per_unit = int(input('Current capacity is 600. Enter new amount: '))

    def __repr__(self):
        self.sizer()
        return "Functional module: Goods to picker\nRequirement: {} order line per hour\nNeeded units: {}".format(self.req_lines_per_hour, self.module_cluster_size)