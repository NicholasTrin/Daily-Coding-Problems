#You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
#record(order_id): adds the order_id to the log
#get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

class log:
    def __init__(self):
        self.log = []
        self.curr_size = -1

    def record(self, order_id):
        self.log.append(order_id)
        self.curr_size += 1

    def get_last(self, i):
        if self.curr_size >= 0:
            return self.log[self.curr_size - i]
        else:
            return "Empty Log"

if __name__ == "__main__":
    log = log()
    print(log.get_last(0))
    log.record("1123")
    print(log.get_last(0))
    log.record("1124")
    log.record("1125")
    log.record("1126")
    log.record("1127")
    print(log.log)
