
class Cpu:
    """Class Processor
    """
    # Attributes:
    id = None  # (int)
    cores = 1  # (int)
    heterogeneous = False  # (bool)
    cunsumed_power = 0  # (float)
    temp = 27  # (float)
    frenquency = None  # (float)
    max_frenquency = None  # (float)
    min_frenquency = None  # (float)

    # Operations
    def run(self):
        """function run

        returns 
        """
        return None  # should raise NotImplementedError()

    def consumed_power(self):
        """function consumed_power

        returns 
        """
        return None  # should raise NotImplementedError()

    def vary_heat(self, temp):
        """function vary_heat

        temp: float

        returns 
        """
        return None  # should raise NotImplementedError()
