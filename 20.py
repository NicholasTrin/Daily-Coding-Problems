# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
#For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
#In this example, assume nodes with the same value are the exact same node objects.
#Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        while self.next:
            print(self.val)
            self = self.next
        print(self.val)



def link_intersect(a, b):
    a_count = 0
    a_temp = a
    while a_temp.next:
        a_count+=1
        a_temp = a_temp.next
    b_count=0
    b_temp = b
    while b_temp.next:
        b_count+=1
        b_temp = b_temp.next

    delta = abs(a_count - b_count)
    if a_count > b_count:
        for skip_node in range(delta):
            a = a.next
    elif b_count > a_count:
        for skip_node in range(delta):
            b = b.next

    while a is not None and b is not None:
        if a is b:
            print(a.val, b.val)
            return a.val
        a = a.next
        b = b.next




intersection_node = Node(5,None)
list_a = Node(1,Node(2,Node(3,Node(4,intersection_node))))
list_b = Node(7,Node(8,Node(9,intersection_node)))
link_intersect(list_a,list_b)

