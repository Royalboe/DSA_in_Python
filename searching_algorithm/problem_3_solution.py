'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. 
You can assume that all the numbers in the list are unique.
'''

def count_rotations_linear(rotated_list):
    position, counts, length = 0, 0, len(rotated_list)
    if length == 0:
        return -1
    while position < length:
        if rotated_list[position] > rotated_list[position + 1]:
            counts += 1
            return counts
        else:
            position += 1
            counts += 1
    return 0

def print_result(rotated_list):
    counts = count_rotations_linear(rotated_list)

    if counts == 0:
        print(f"List was not rotated")
    elif counts > 0:
        print(f"List was rotated at least {counts} times")
    else:
        print("List is empty")