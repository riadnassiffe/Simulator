class Scheduler(object):
   
    def __init__(self, env, cpu_list=[], task_list=[]):
        self.env = env
        self.cpu_list = cpu_list
        self.task_list = []
        self._lock = False
        self.overhead = 0


    def run(self):
        pass

    def on_activate(self, job):
        pass

    def on_terminated(self, job):
        pass

    def schedule(self, cpu):
        raise NotImplementedError("You need to everride the schedule method!")

    def add_task(self, task):
        self.task_list.append(task)

    def add_processor(self, cpu):
        self.cpu_list.append(cpu)