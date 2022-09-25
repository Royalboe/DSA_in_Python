''' A function for linear search 
    It has a big O of O(N) which is a complexity of linear time
'''


def linear_search(list_a, query):
    position = 0
    while position < len(list_a):
        if list_a[position] == query:
            return position
        position += 1
    return -1
