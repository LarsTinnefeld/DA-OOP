class Functional_module():

    def __init__(self, req_units_per_hour, req_lines_per_hour,module_cluster_size = 1, cost_per_unit = 1):
        self.req_units_per_hour = req_units_per_hour
        self.req_lines_per_hour = req_lines_per_hour
        self.module_cluster_size = module_cluster_size
        self.cost_per_unit = cost_per_unit

    def calculate_cost(self):
        '''This method calculates the cost of the cluster.'''

        self.total_cost = self.cost_per_unit * self.module_cluster_size
        return self.total_cost
