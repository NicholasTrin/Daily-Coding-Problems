# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

#XOR operation is nullified when XOR is performed between two of the same values. Eg. A XOR B XOR A = B
#


class Node:
    def __init__(self,val):
        self.val = val
        self.pointer = 0

    def append_element(self, node)->None:
        if self.pointer == 0:
            self.pointer = self.pointer ^ node
            node.pointer = node.pointer ^ self
        else:
            prev_node = 0
            while self.pointer ^ prev_node != 0:
                temp_node = self
                self = self.pointer ^ prev_node
                prev_node = temp_node
            self.pointer = self.pointer ^ node
            node.pointer = node.pointer ^ self

    def node_index(self, index):
        prev_node = 0
        while self.pointer ^ prev_node != 0:
            if index == 0:
                return self
            temp_node = self
            self = self.pointer ^ prev_node
            prev_node = temp_node
            index -= 1
        return -1