# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively expensive.
# Do this in constant space and in one pass.

class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

    def remove_k(self,k):
        for i in range(k):
            prev_node = self
            self = self.next
        if self:
            prev_node.next = self.next
        else:
            prev_node.next = None

    def __str__(self):
        print("List",end=':')
        while self:
            print(self.val, end='->')
            self = self.next
        print("End of List")



list = Node(0,Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,None)))))))
list.__str__()
list.remove_k(6)
list.__str__()