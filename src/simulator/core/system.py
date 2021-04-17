from typing import List, Optional
from .components.logger import Logger
from .components.task import Task
from .components.scheduler import Scheduler
from .components.cpu import Cpu
import simpy


class System:
    """Class System
    """
    # Operations

    def __init__(self, scheduler: Scheduler, temperature: int, name: str) -> None:
        """
        """
        self.__env = simpy.Environment()
        self.__temperature = temperature  # (int)
        self.__task_list = []  # (list)
        self.__cpu_list = []  # (list)
        self.__devices_power = 0  # (int)
        self.name = None  # (string)
        self.__reconfiguration = None  # (bool)
        self.__total_power_consumption = None  # (int)
        self.__log = None  # (Logger)
        self.__scheluder = None  # (Scheluder)

    def append_task(self, task: Task) -> None:
        """Append a Task object to the simulation task list.

        :param task: a task object.
        :type task: Task
        """
        self.__task_list.append(task)

    def get_task(self, index: int) -> Optional[Task]:
        """Get a task object by index

        :param index: [description]
        :type index: int
        :return: [description]
        :rtype: Task
        """
        if index < len(self.__task_list):
            return self.__task_list[index]

    @property
    def num_tasks(self) -> int:
        """[summary]

        :return: [description]
        :rtype: int
        """
        return len(self.__task_list)

    def del_task(self, task: Task) -> bool:
        """[summary]

        :param task: [description]
        :type task: Task
        :return: [description]
        :rtype: bool
        """
        try:
            self.__task_list.remove(task)
        except:
            return False
        return True

    def append_cpu(self, cpu: Cpu) -> None:
        """Append a Cpu object to the simulation CPU list.

        :param cpu: [description]
        :type cpu: Cpu
        """
        self.__cpu_list.append(Cpu)

    def run(self, time=1):
        # Creating resources for each processor
        # the problem is that resources works with FIFO policy.
        processors = simpy.Resource(self.env, capacity=len(self.cpu_list))

        self.env.run(until=time)
        return None  # should raise NotImplementedError()
