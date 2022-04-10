#This problem was asked by Amazon.
#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
#For example, given s = "abacba" and k = 2, the longest substring with k distinct characters is "bcb".

def longest_substring(str_,unique_char_count)->str:
    unique_char_in_string = 0
    curr_string = ''
    largest_string = ''

    for i in range(len(str_)):
        if str_[i] in curr_string:
            curr_string += str_[i]
        elif unique_char_count != unique_char_in_string:
            unique_char_in_string += 1
            curr_string += str_[i]
        else:
            if len(largest_string) < len(curr_string):
                largest_string = curr_string
            curr_string = curr_string[curr_string.rfind(curr_string[0])+1:] + str_[i]
            unique_char_in_string = len(set(curr_string))
    return largest_string


if __name__ == "__main__" :
    print(longest_substring("abacba",2))
