# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

def bracket_parser(string: str) -> bool:
    bracket_list = []
    closing_brackets = [']', '}', ')']
    opening_brackets = ['[', '{', '(']
    for bracket in string:
        if bracket in opening_brackets:
            bracket_list.append(bracket)
        else:
            opening_bracket = bracket_list.pop()
            closing_bracket_index = closing_brackets.index(bracket)
            if opening_bracket != opening_brackets[closing_bracket_index]:
                return False
    return True

test ='([])[]({})'
print(bracket_parser(test))
test ='([)]'
print(bracket_parser(test))