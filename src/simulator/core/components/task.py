from .system import System
from .job import Job


class IdGenerator:

    def __init__(self):
        self.id = 0

    def next(self):
        self.id += 1
        return  self.id

class Task:
    """Class Task
    """
    __last_id = IdGenerator()
    
    # Operations
    def __init__(self, abort_on_miss: bool, end_time: int,
                 wcet: int, deadline: int, period: int, 
                 start_time: int = 0):
        """ Create a task.
        
        This method initialize a task object.

        Parameters
        ----------
        
        :param abort_on_miss: This parameter indicates that the task will be 
            aborted if loses deadline. (default is False)
        :type abort_on_miss: bool 
        start_time (int): (default is 0)

        end_time (int):
        
        wcet (int):
        
        deadline (int):
        
        start_time (int): (default is 0)

        period (int):

        Raises
        ------
        IvalidParameter
            If any parameter is invalid. 
        """
        # Attributes:
        self.__tardness = 0
        self.__id = self.__last_id.next()
        self.__abort_on_miss = abort_on_miss
        self.__start_time = start_time
        self.__end_time = None 
        self.__wcet = None 
        self.__deadline = deadline 
        self.__job_list = [] 
        self.__period = period

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
    

