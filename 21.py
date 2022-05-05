#Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
#For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
import math


def get_min_rooms(time_slots:list)->int:
    hash_map = {}
    start_classes, stop_classes = math.inf,0
    for time_slot in time_slots:
        start,stop = time_slot
        if start_classes > start:
            start_classes = start
        if stop_classes < stop:
            stop_classes = stop
        if hash_map.get(start):
            hash_map[start] += 1
        else:
            hash_map[start] = 1
        if hash_map.get(stop):
            hash_map[stop] -= 1
        else:
            hash_map[stop] = -1
    min_rooms, active_classes = 0, 0
    for i in range(start_classes, stop_classes+1):
        if hash_map.get(i):
            active_classes += hash_map.get(i)
        if min_rooms < active_classes:
            min_rooms = active_classes
    return min_rooms


rooms = [(30, 75), (0, 50), (60, 150),(170,180),(175,180)]
print(get_min_rooms(rooms))
