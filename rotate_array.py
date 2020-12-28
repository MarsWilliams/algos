from typing import List


def rotate_array(nums: List[int], k):
    """rotate array to the right k times
    """
    net_shifts = k % len(nums)
    for i in range(net_shifts):
        temp = nums.pop()
        nums = [temp] + nums
    return nums


assert rotate_array([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
assert rotate_array([-1, -100, 3, 99], 1) == [99, -1, -100, 3]
assert rotate_array([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]

