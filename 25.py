# Implement regular expression matching with the following special characters:
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element

def match(expression: str, string: str, index_exp, index_string,counter=0) -> bool:
    if index_exp < 0 and index_string < 0:
        print(counter)
        return True

    if string[index_string] == expression[index_exp] or expression[index_exp] == '.':
        return match(expression, string, index_exp - 1, index_string - 1,counter+1)

    if expression[index_exp] == '*':
        if index_exp > 0:
            if expression[index_exp - 1] == '.':
                temp_index = index_string
                temp_char = string[index_string]
                while string[temp_index] == temp_char:
                    temp_index -= 1
                    counter += 1
                return match(expression, string, index_exp - 1, temp_index,counter)
            elif expression[index_exp - 1] == string[index_string]:
                temp_index = index_string
                temp_char = string[index_string]
                while string[temp_index] == temp_char:
                    temp_index -= 1
                    counter+=1
                return match(expression, string, index_exp - 2, temp_index,counter)
            else:
                return match(expression, string, index_exp - 1, index_string,counter+1)
        else:
            return match(expression, string, index_exp - 1, index_string,counter+1)
    print(counter)
    return False


expression = 'ra.'
string = 'ray'
print(match(expression, string, len(expression) - 1, len(string) - 1))
expression = 'ra.'
string = 'rays'
print(match(expression, string, len(expression) - 1, len(string) - 1))
expression = '.*at'
string = 'chat'
print(match(expression, string, len(expression) - 1, len(string) - 1))
expression = '*ao*f'
string = 'aooof'
print(match(expression, string, len(expression) - 1, len(string) - 1))
expression = 'ch*ta.'
string = 'chhhhtaz'
print(match(expression, string, len(expression) - 1, len(string) - 1))
expression = '.*f'
string = 'wooooooooooooooooooooooooooooooof'
print(match(expression, string, len(expression) - 1, len(string) - 1))