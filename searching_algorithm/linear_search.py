''' A function for linear search '''

def linear_search(list_a, query):
    position = 0
    while position < len(list_a):
        if list_a[position] == query:
            return position
        position += 1
    return -1
