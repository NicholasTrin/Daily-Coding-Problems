# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        print(self.val)
        if self.left and self.right is not None:
            self.left.print_tree()
            self.right.print_tree()

    def unival_count(self):
        if self.left:
            count_left, left_is_unival = self.left.unival_count()
        if self.right:
            count_right, right_is_unival = self.right.unival_count()

        # Leaf Node (2x Nones)
        if self.right is None and self.left is None:
            return 1, False
        # Node with leaf and None
        elif (self.left is None and self.right is not None) or (self.right is None and self.left is not None):
            is_unival = False
        # Unival block (Node and leaf all same values)
        elif self.left.val == self.right.val == self.val:
            is_unival = True
        # Non-unival block (Node and leafs differ in values)
        else:
            is_unival = False

        if left_is_unival and right_is_unival and is_unival:
            return count_left + count_right + is_unival + 1, True
        else:
            return count_left + count_right + is_unival, False

def main():
    root = Node(1, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(1, Node(1), Node(1))))
    print(root.unival_count())
    root = Node(0, Node(1), Node(1))
    print(root.unival_count())


if __name__ == '__main__':
    main()
