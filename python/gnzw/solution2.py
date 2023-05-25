#!/usr/bin/env python

def solution(target, nums, start, end):
    # print('start: {}, end: {}'.format(start, end))
    if start == end:
        if nums[start] == target:
            return start
        else:
            return -1


    index = int((start + end) / 2)
    if target > nums[index]:
        return solution(target, nums, index+1, end)
    else:
        return solution(target, nums, start, index)


if __name__ == '__main__':
    print(solution(2, [1, 3, 3, 3, 4, 4, 5], 0, 6))
