# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

def lowest_positive_integer(set)->int:

    #Shift negative values to the right
    max_pos_int = len(set)
    for i in range(len(set)-1,-1,-1):
        if set[i] <= 0:
            max_pos_int -= 1
            set[i], set[max_pos_int] = set[max_pos_int], set[i]
    print(set)
    for i in range(0, max_pos_int):
        if abs(set[i]) - 1 < max_pos_int and set[abs(set[i])-1] > 0:
            set[abs(set[i])-1] = -set[abs(set[i]) - 1]


    for i in range(max_pos_int):
        if set[i] > 0:
            return i+1
    return max_pos_int+1


def main():
    sample_set_1= [3, -1, 4, 1,5,1,-3,1,-24,-3,5,2,5]
    sample_set_2 = [0,3,1]
    print(lowest_positive_integer(sample_set_1))
    print(lowest_positive_integer(sample_set_2))


if __name__ == '__main__':
    main()