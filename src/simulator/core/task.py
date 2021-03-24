from system import System
from job import Job

class Task:
    """Class Task
    """
    # Attributes:
    tardness = None  # (int) 
    __id = None  # (int) 
    __abort_on_miss = None  # (bool) 
    __start_time = None  # (int) 
    __end_time = None  # (int) 
    __wcet = None  # (int) 
    __deadline = None  # (int) 
    __last_id = 0  # (int) 
    __priority = 0  # (int) 
    __job_list = []  # (Job) 
    
    # Operations
    def __init__(self, abort_on_miss, start_time = 0, end_time, wcet, deadline):
        """function __init__
        
        abort_on_miss: bool
        start_time: int
        end_time: int
        wcet: int
        deadline: int
        
        returns 
        """
        return None # should raise NotImplementedError()
    
    def generate_job(self, ):
        """function generate_job
        
        : 
        
        returns Job
        """
        return None # should raise NotImplementedError()
    
    def total_job_exec_time(self):
        """function total_job_exec_time
        
        returns int
        """
        return None # should raise NotImplementedError()
    
    def total_deadline_miss(self):
        """function total_deadline_miss
        
        returns 
        """
        return None # should raise NotImplementedError()
    

