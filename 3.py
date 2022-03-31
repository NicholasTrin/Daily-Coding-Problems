# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(string_):
    val = Node(string_[1:string_.index(',')])
    string_ = string_[string_.index(',')+1:]
    print(string_)
    if string_[1:string_.index(',')] != 'None':
        left = deserialize(string_)
    else:
        left = None
    print(val,left)


def serialize(node):
    val = node.val
    if node.left:
        left = serialize(node.left)
    else:
        left = 'None'
    if node.right:
        right = serialize(node.right)
    else:
        right = 'None'
    return "({},{},{})".format(val,left,right)


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized_string = serialize(node)
    print(serialized_string)
    deserialize(serialized_string)

    # assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == "__main__":
    main()
