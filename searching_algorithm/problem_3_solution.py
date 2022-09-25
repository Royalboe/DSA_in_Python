'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. 
You can assume that all the numbers in the list are unique.
'''


def count_rotations_linear(rotated_list):
    position, length = 0, len(rotated_list)
    if length == 0:
        return -1
    while position < length:
        if position > 0 and rotated_list[position] < rotated_list[position - 1]:
            return position
        else:
            position += 1
    return 0


'''
An helper function for the binary search solution

'''


def binary_search(lo, hi, condition):
    '''TODOS'''
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


"""
A function that employs binary search to solve the problem
"""


def count_rotations_binary(rotated_list):
    length = len(rotated_list)

    def condition(mid):
        middle_number = rotated_list[mid]
        if length > 1:
            if middle_number < rotated_list[mid - 1]:
                return 'found'
            elif middle_number > rotated_list[length - 1]:
                return 'right'
            else:
                return 'left'
        elif length == 1:
            return 'found'
        else:
            return -1

    return binary_search(0, len(rotated_list) - 1, condition)


"""
An helper fxn that prints the solution to the screen
"""


def print_result(rotated_list, count_rotations):
    counts = count_rotations(rotated_list)

    if counts == 0:
        print(f"List was not rotated")
    elif counts > 0:
        print(f"List was rotated at least {counts} times")
    else:
        print("List is empty")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rotated_list_a = [2, 3, 4, 5, 1]
    print_result(rotated_list_a, count_rotations_linear)
    print_result(rotated_list_a, count_rotations_binary)