# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}


class trie:

    def __init__(self):
        self.children = {}

    def insert_word(self, word):
        curr_node = self
        for char in word:
            char_index = ord(char) - 96
            if curr_node.children.get(char_index) is None:
                curr_node.children[char_index] = Node(char)
            curr_node = curr_node.children[char_index]

    def prefix_match(self,prefix)->list:
        list_product = []
        curr_node = self

        for char in prefix:
            char_index = ord(char) - 96
            if curr_node.children.get(char_index):
                curr_node = curr_node.children.get(char_index)
            else:
                return [None]

        list_product.extend([prefix+postfix for postfix in self.helper(curr_node).split('~')])
        return list_product[:len(list_product)-1]

    def helper(self, node)->str:
        ret_string = ''
        for i in node.children:
            if node.children.get(i).children:
                ret_string += node.children.get(i).val + self.helper(node.children.get(i))
            else:
                ret_string += node.children.get(i).val + "~"
        return ret_string

    def print_trie(self, node=None):
        if node is None:
            for i in self.children:
                print(self.children.get(i).val)
                self.print_trie(self.children.get(i))
        else:
            for i in node.children:
                print(node.children.get(i).val)
                self.print_trie(node.children.get(i))


if __name__ == '__main__':
    data_struc = trie()
    data_struc.insert_word('woof')
    data_struc.insert_word('woaf')
    data_struc.insert_word('wafer')
    data_struc.insert_word('completelywrong')
    data_struc.insert_word('wooooooooooooooooooooooof')
    print(data_struc.prefix_match('wo'))

