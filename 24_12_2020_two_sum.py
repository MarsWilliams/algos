from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    addends = {}
    for i, num in enumerate(nums):
        addend = target - num

        if addend in addends:
            return [i, addends[addend]]

        else:
            addends[num] = i

    return []


assert set(two_sum([1, 2, 3, 4], 7)) == {2, 3}
