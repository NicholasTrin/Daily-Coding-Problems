#Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

from random import randint,random

def rand_element(stream):
    rand_char = ''
    rand_distribution = -1

    for char in stream:
        if char == '':
            rand_char = stream[0]
        else:
            temp = random()
            if rand_distribution < temp:
                rand_distribution = temp
                rand_char = char
    return rand_char

if __name__ == "__main__":
    stream = "abcdefghijklmnopqrstuvwxyz"
    map = {}
    for i in range(0,100000):
        curr_char = rand_element(stream)
        if map.get(curr_char):
            map[curr_char] = map.get(curr_char) + 1
        else:
            map[curr_char] = 1
    print(map)
