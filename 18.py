#Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

def max_subarray_values(integers, sub_array_length) -> list:
    num_subarrays = len(integers) - sub_array_length + 1
    for i in range(num_subarrays):
        print(max(integers[i:i+sub_array_length]))



if __name__ == "__main__":
    array = [10,5,2,7,8,7,10,23,1,2,1]
    max_subarray_values(array,3)