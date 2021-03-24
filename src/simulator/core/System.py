from Logger import Logger

class System:
    """Class System
    """
    # Attributes:
    temperature = None  # (int) 
    task_list = None  # (list) 
    cpu_list = None  # (list) 
    devices_power = 0  # (int) 
    name = None  # (string) 
    reconfiguration = None  # (bool) 
    total_power_consumption = None  # (int) 
    log = None  # (Logger) 
    scheluder = None  # (Scheluder) 
    
    # Operations
    def __init__(self, cpu_list, scheduler, temperature, name, ):
        """function __init__
        
        cpu_list: list
        scheduler: Scheduler
        temperature: 20
        name: device_power
        : 
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def run(self):
        """function run
        
        returns 
        """
        return None # should raise NotImplementedError()
    

