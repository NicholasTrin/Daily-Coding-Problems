class Node:
    def __init__(self, val, left: 'Node' = None, right: 'Node' = None, parent: 'Node' = None, lock_state=False):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent
        self.lock_state = lock_state

    # True: parent/sub-nodes have lock(s)
    # False: parent/sub-nodes are unlocked
    def get_lock_state_change(self) -> bool:
        def children_state(current_node):
            left_node, right_node = False, False
            if current_node.left:
                left_node = children_state(current_node.left)
            if current_node.right:
                right_node = children_state(current_node.right)
            return left_node + right_node + current_node.is_locked()

        def parent_state(current_node):
            parent = False
            if current_node.parent:
                parent = parent_state(current_node.parent)
            return current_node.is_locked() + parent

        parents, child_right, child_left = False,False,False
        if self.parent:
            parents = parent_state(self.parent)
        if self.left:
            child_left = children_state(self.left)
        if self.right:
            child_right = children_state(self.right)
        return child_right + child_left + parents

    def is_locked(self):
        return self.lock_state

    def locked(self):
        if self.get_lock_state_change():
            return False
        else:
            self.lock_state = True
            return True

    def unlock(self):
        if self.get_lock_state_change():
            return False
        else:
            self.lock_state = False
            return True

    def print_tree(self):
        print(self.val)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


binary_tree = Node(1)
binary_tree.left = Node(2, None, None, binary_tree)
binary_tree.right = Node(3, None, None, binary_tree)
binary_tree.right.right = Node(4, None, None, binary_tree.right)


print(binary_tree.locked())
print(binary_tree.locked())
print(binary_tree.unlock())

binary_tree.left.lock_state = True

print(binary_tree.locked())
print(binary_tree.unlock())


print(binary_tree.left.unlock())