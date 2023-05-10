#!/usr/bin/python

min_index = None

def binary_search(array, n):
    def _binary_search(array, start, end, n):
        global min_index
        if start == end:
            if array[start] == n:
                if min_index is None or start < min_index:
                    min_index = start
        elif end > start:
            mid = (start + end) / 2
            if array[mid] == n:
                if min_index is None or start < min_index:
                    min_index = mid
            if array[mid] >= n:
                _binary_search(array, start, mid, n)
            else:
                _binary_search(array, mid+1, end, n)
    _binary_search(array, 0, len(array)-1, n)

    if min_index is None:
        return -1
    return min_index


if __name__ == '__main__':
    array = [1, 1, 2, 2, 3, 3, 4, 5, 6]
    n = 2
    find = binary_search(array, n)
    print(find)
