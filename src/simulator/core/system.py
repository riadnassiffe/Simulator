from componentes.logger import Logger
from simpy

class System:
    """Class System
    """
    # Operations
    def __init__(self, scheduler, temperature, name):
        """function __init__
        
        cpu_list: list
        scheduler: Scheduler
        temperature: 20
        name: device_power
        : 
        
        returns 
        """
        self.env = simpy.Environment()
        self.temperature = temperature  # (int) 
        self.task_list = []  # (list) 
        self.cpu_list = []  # (list) 
        self.devices_power = 0  # (int) 
        self.name = None  # (string) 
        self.reconfiguration = None  # (bool) 
        self.total_power_consumption = None  # (int) 
        self.log = None  # (Logger) 
        self.scheluder = None  # (Scheluder) 
    
    def run(self, time=1):
        #Creating resources for each processor
        #the problem is that resources works with FIFO policy.
        processors = simpy.Resource(self.env, capacity=len(self.cpu_list))  


        self.env.run(until=time)
        return None # should raise NotImplementedError()
    

