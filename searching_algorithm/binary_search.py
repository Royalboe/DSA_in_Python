''' A function for binary search 
    It has a big O of O(log N) which is a complexity of logarithmic time
'''

'''
## Generic Binary Search

Here is the general strategy behind binary search, which is applicable to a variety of problems:

1. Come up with a condition to determine whether the answer lies before, after or at a given position
1. Retrieve the midpoint and the middle element of the list.
2. If it is the answer, return the middle position as the answer.
3. If answer lies before it, repeat the search with the first half of the list
4. If the answer lies after it, repeat the search with the second half of the list.

Here is the generic algorithm for binary search, implemented in Python:
'''


def binary_search(lo, hi, condition):
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
    return binary_search(0, len(list_a) - 1, condition)