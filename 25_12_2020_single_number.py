from typing import List
from collections import Counter


def single_number(nums: List[int]) -> int:
    return (k for k, v in Counter(nums).items() if v == 1).__next__()


assert single_number([4, 1, 2, 1, 2]) == 4


def single_number_set(nums: List[int]) -> int:
    singles = set()
    for i in nums:
        if i in singles:
            singles.remove(i)
        else:
            singles.add(i)
    return singles.pop()


assert single_number_set([4, 1, 2, 1, 2]) == 4


def single_number_math(nums: List[int]) -> int:
    """2∗(a+b+c)−(a+a+b+b+c)=c"""
    return 2*sum(set(nums))-sum(nums)


assert single_number_math([4, 1, 2, 1, 2]) == 4
