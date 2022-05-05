#Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

from collections import deque
#O(N^2)
def max_subarray_values(integers, sub_array_length):
    num_subarrays = len(integers) - sub_array_length + 1
    for i in range(num_subarrays):
        print(max(integers[i:i+sub_array_length]))


def printMax(arr, n, k):
    """ Create a Double Ended Queue, Qi that
    will store indexes of array elements.
    The queue will store indexes of useful
    elements in every window and it will
    maintain decreasing order of values from
    front to rear in Qi, i.e., arr[Qi.front[]]
    to arr[Qi.rear()] are sorted in decreasing
    order"""
    Qi = deque()

    # Process first k (or first window)
    # elements of array
    for i in range(k):

        # For every element, the previous
        # smaller elements are useless
        # so remove them from Qi
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        # Add new element at rear of queue
        Qi.append(i);

    print(Qi)
    # Process rest of the elements, i.e.
    # from arr[k] to arr[n-1]
    for i in range(k, n):

        # The element at the front of the
        # queue is the largest element of
        # previous window, so print it
        print(str(arr[Qi[0]]) + " ", end="")

        # Remove the elements which are
        # out of this window
        while Qi and Qi[0] <= i - k:
            # remove from front of deque
            Qi.popleft()

        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()

        # Add current element at the rear of Qi
        Qi.append(i)

    # Print the maximum element of last window
    print(str(arr[Qi[0]]))


if __name__ == "__main__":
    array = [10,5,2,7,8,7,10,23,1,2,1]
    #max_subarray_values(array,3)
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    printMax(arr, len(arr), k)