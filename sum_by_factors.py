"""
Task:
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]

See: https://www.codewars.com/kata/54d496788776e49e6b00052f
"""

def sum_for_list(lst):
    from collections import defaultdict
    result = defaultdict(int)
    nums = [abs(i) for i in lst]

    divides_by_2 = [i for i in lst if i%2==0]
    result[2] = sum(divides_by_2)
    for num in (abs(i) for i in divides_by_2):
        cur_n = num
        while cur_n%2 == 0:
            cur_n //= 2
        if cur_n == 1:
            nums.remove(num)
        else:
            nums[nums.index(num)] = cur_n

    for p in range(3, max(nums), 2):
        p_is_factor = [i for i in nums if i%p==0]
        if p_is_factor:
            print(p)
            result[p] = sum(i for i in lst if i%p==0)
            for num in p_is_factor:
                cur_n = num
                while cur_n%p == 0:
                    cur_n //= p
                if cur_n == 1:
                    nums.remove(num)
                else:
                    nums[nums.index(num)] = cur_n

        if not nums:
            print("We broke")
            break

        if p>(max(nums))**0.5:
            for n in nums:
                result[n] = sum(i for i in lst if i%n==0)
            break


    return sorted([[i, result[i]] for i in result])