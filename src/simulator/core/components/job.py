
class Job(object):
    """Class Job
    """
    # Attributes:
    def __init__(self, env, executed_time, released_time, execution_time, consumed_power, assined_cpu):
    self.env = env
    self.executed_time = executed_time  # (int) 
    self.released_time = released_time  # (int) 
    self.execution_time = execution_time  # (int) 
    self.consumed_power = consumed_power  # () 
    self.started_time = 0
    self.assined_cpu = assined_cpu
    self.action = self.env.process(self.run())
    
    # Operations
    def run(self):
        self.started_time = self.env.now()
        yield self.env.timeout(self.execution_time)
        self.executed_time = self.env.now() - self.started_time()
    

