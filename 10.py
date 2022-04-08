from time import time
import threading

class Scheduler:
    def __init__(self):
        self.to_call = []
        self.scheduler_thread = threading.Thread(target=self._initiate)
        self.scheduler_thread.start()


    def _initiate(self):
        while True:
            curr_time = time()*1000
            for i in self.to_call:
                func, time_due, args = i
                if curr_time >= time_due:
                    func(*args)
                    self.to_call.remove(i)
                    self.to_call = [to_call for to_call in self.to_call if to_call]

    def add_call(self,func,delay,*args):
        self.to_call.append([func, delay + time()*1000, args])


def random_call(a,b,c):
    print(time())
    print(a+b+c)


if __name__ == '__main__':
    sched = Scheduler()
    sched.add_call(random_call,1000,1,2,3)
    sched.add_call(random_call, 1000, 1, 2, 3)
    sched.add_call(random_call, 2000, 1, 2, 3)
    sched.add_call(random_call, 4000, 1, 2, 3)














#

