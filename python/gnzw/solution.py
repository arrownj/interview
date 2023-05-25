#!/usr/bin/env python

def solution(nums):
    return_length = 0
    max_num = 0
    last_num = 0
    longest_length = 0
    for n in nums:
        if n > max_num:
            max_num = n
            longest_length = 1
        if n == max_num:
            if n == last_num:
                longest_length +=1
        else:
            longest_length = 0
            max_num = 0
        if return_length < longest_length:
            return_length = longest_length
        last_num = n
    return return_length



if __name__ == '__main__':
    print(solution([1, 2, 3, 3, 2, 2]))
    print(solution([1, 2, 3, 3, 2, 2, 3, 3, 3]))
    print(solution([1, 2, 3, 4]))

