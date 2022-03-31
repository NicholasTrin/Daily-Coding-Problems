# Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

# Time O(N), space O(n)
def non_inclusive_product(list_) -> list:
    list_product = 1
    modified_list = [1] * len(list_)

    for i in list_:
        list_product *= i

    for i in range(len(list_)):
        modified_list[i] *= int(list_product / (list_[i]))

    return modified_list


# Without division, less clck cycles

# Time O(N^2), space O(N)
def non_inclusive_product_2(list_) -> list:
    modified_list = [1] * len(list_)
    for i in range(len(list_)):
        for j in range(len(list_)):
            if i != j:
                modified_list[j] *= list_[i]
    return modified_list


# Time and space O(n)
def non_inclusive_product_3(list_) -> list:
    modified_list = [1] * len(list_)

    right_shifted_factorial = [1] * len(list_)
    for i in range(1, len(list_), 1):
        right_shifted_factorial[i] *= list_[i - 1] * right_shifted_factorial[i - 1]

    left_shifted_factorial = [1] * len(list_)
    for j in range(len(list_) - 1, 0, -1):
        left_shifted_factorial[j - 1] *= list_[j] * left_shifted_factorial[j]

    for k in range(len(list_)):
        modified_list[k] = right_shifted_factorial[k] * left_shifted_factorial[k]

    return modified_list


def main():
    numbers = [1, 2, 3, 4, 5]
    print(non_inclusive_product(numbers))
    numbers = [1, 2, 3, 4, 5]
    print(non_inclusive_product_3(numbers))


if __name__ == "__main__":
    main()
