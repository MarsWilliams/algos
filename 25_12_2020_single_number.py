from typing import List
from collections import Counter


def single_number(nums: List[int]) -> int:
    return [k for k, v in Counter(nums).items() if v == 1][0]


assert single_number([4, 1, 2, 1, 2]) == 4
