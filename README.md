# Another Real Time Scheduler

## System objectives:

      * Simulate an EDF or CBS scheduler;
      * The system should support two types o tasks, tasks with device time and without device time;
      * System should support a single core CPU with energy and temperature models;
      * Tasks should be generated at least with UNNIFAST algorithm;
      * Extra devices energy should be take in consideration;
      * CPU time to switch frequency must be counted.

## Implemented:
* Rate Monotonic (RM) scheduler;
* Basic component abstractions (Job, Task, Scheduler);
* Basic CPU abstraction class.

## To be implemented:
* EDF or CBS schedulers;
* Support for tasks with and without device time;
* Concrete implementation of a single core CPU with energy and temperature models;
* Task generation with UNNIFAST algorithm;
* Consideration of extra devices energy;
* Counting of CPU time to switch frequency.
