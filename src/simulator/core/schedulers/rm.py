from core.components.scheduler import Scheduler

class Rm(Scheduler)

    def run(self):
        self.ready_list = []

    def on_activate(self, job):
        self.ready_list.append(job)
        job.cpu.resched()

    def on_terminated(self, job):
        self.ready_list.remove(job)
        job.cpu.resched()

    def schedule(self):
        if self.ready_list:
            job = min(self.ready_list, key=lambda x: x.period)
        else:
            job = None

        return job