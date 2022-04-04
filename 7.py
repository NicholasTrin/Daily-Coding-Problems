# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.


def decode_possibilities(code)->int:
    possibilities = 1
    prev_val = 0
    for i in range(len(code)):
        if prev_val != 0 and int(prev_val+code[i]) <= 26:
            possibilities += 1
        prev_val = code[i]
    return possibilities

def main():
    code = '111'
    print(decode_possibilities(code))
    code = '6257'
    print(decode_possibilities(code))
    code = '6212'
    print(decode_possibilities(code))

if __name__ == '__main__':
    main()
