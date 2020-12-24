from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.
    """
    addends = {}
    for i, num in enumerate(nums):
        addend = target - num

        if addend in addends:
            return [i, addends[addend]]

        else:
            addends[num] = i

    return []


assert set(two_sum([1, 2, 3, 4], 7)) == {2, 3}
