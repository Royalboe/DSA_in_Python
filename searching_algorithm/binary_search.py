''' A function for binary search 
    It has a big O of O(log N) which is a complexity of logarithmic time
'''


def binary_serach(lo, hi, condition):
    '''TODOS'''
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        else:
            lo = mid + 1
    return -1


def locate_query(list_a, query):
    def condition (mid):
        if list_a[mid] == query:
            if mid > 0 and list_a[mid -1] == query:
                return 'left'
            else:
                return 'found'
        elif list_a[mid] < query:
            return 'left'
        else:
            return 'right'
    return binary_serach(0, len(list_a) - 1, condition)