# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Time and space O(N)

def sum_to_k(numbers, k) -> bool:
    hash_map = {}
    for i in range(len(numbers)):
        if k - numbers[i] in hash_map.values():
            return True
        else:
            hash_map[i] = numbers[i]
    return False


def main():
    numbers = [10, 15, 3, 7]
    numbers2 = [10, 15, 3, 6]
    k = 17
    print(sum_to_k(numbers, k))
    print(sum_to_k(numbers2, k))

if __name__ == "__main__":
    main()
