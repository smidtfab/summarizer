import schedule
import time
import sys

class Scheduler:

    ''' TODO: Set up timestamp'''
    def __init__(self):
        pass

    def job(self, t):
        print("I'm working...", t)
        return

    def define_schedule(self, scheduled_time):
        schedule.every().day.at(scheduled_time).do(scheduler.job, "job")

        while True:
            schedule.run_pending()
            time.sleep(60) # wait one minute

if __name__ == "__main__":
    if len(sys.argv) == 2:
        scheduled_time = sys.argv[1]
        scheduler = Scheduler()
        scheduler.define_schedule(scheduled_time)
    else:
        raise ValueError("Please enter a time for the schedule of format hh:mm")