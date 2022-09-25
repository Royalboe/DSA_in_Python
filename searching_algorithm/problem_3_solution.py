"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list.
You can assume that all the numbers in the list are unique.
"""


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
    """TODOS"""
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


def count_rotations_binary(rotated_list, target=-2):
    length = len(rotated_list)

    def condition(mid):
        middle_number = rotated_list[mid]
        if length > 1:
            if middle_number < rotated_list[mid - 1]:
                return 'found'
            elif middle_number > rotated_list[length - 1]:
                return 'right'
            elif mid == 0 and middle_number == rotated_list[0]:
                return 'found'
            else:
                return 'left'
        elif length == 1:
            return 'found'
        else:
            return -1

    if target > -2:
        first_element_index = binary_search(0, len(rotated_list) - 1, condition)
        return [get_target_position(rotated_list, first_element_index, target), first_element_index]

    return binary_search(0, len(rotated_list) - 1, condition)


def get_target_position(rotated_list, element_index, target):
    if element_index > 0:
        list_a = rotated_list[:element_index]
        list_b = rotated_list[element_index:]

        result_a = is_present(list_a, target)
        result_b = is_present(list_b, target)

        if result_a >= 0:
            return result_a
        elif result_b >= 0:
            return result_b + element_index
        else:
            return 'target not present'

    return is_present(rotated_list, target)


def is_present(new_list, target):

    def condition(mid):
        mid_num = new_list[mid]
        if mid_num == target:
            if mid > 0 and new_list[mid - 1] == target:
                return 'left'
            return 'found'
        elif mid_num < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(new_list) - 1, condition)


"""
An helper fxn that prints the solution to the screen
"""


def print_result(rotated_list, count_rotations, target=-2):
    if target == -2:
        counts = count_rotations(rotated_list)

        if counts == 0:
            print(f"List was not rotated")
        elif counts > 0:
            print(f"List was rotated at least {counts} times")
        else:
            print("List is empty")
    else:
        counts = count_rotations(rotated_list, target)
        if counts[0] == 0:
            print(f"List was not rotated, target was in position {counts[1]}")
        elif counts[0] > 0:
            print(f"List was rotated at least {counts[1]} times, target was in position {counts[0]}")
        else:
            print("List is empty")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rotated_list_a = [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]
    print_result(rotated_list_a, count_rotations_linear)
    print_result(rotated_list_a, count_rotations_binary)
    print_result(rotated_list_a, count_rotations_binary, 2)
