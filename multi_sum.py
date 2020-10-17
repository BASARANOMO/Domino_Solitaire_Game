"""
@Author: ZHANG Mofan
@Time: 09/29/2020 22:00-23:00
"""

import numpy as np


def two_sum(nums, target):
    """ return indices of the two numbers such that they add up to target

    Parameters
    ----------
    nums
    target

    Returns
    -------
    list

    """
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]


def three_sum(nums, target):
    """

    Parameters
    ----------
    nums
    target

    Returns
    -------

    """
    sort_idx_list = np.argsort(nums)
    nums.sort()
    len1 = len(nums)
    if len1 <= 2:
        return []
    for i in range(len1 - 1):
        left, right = i + 1, len1 - 1  # inspired by quick sort
        while left < right:
            temp = nums[i] + nums[left] + nums[right]
            if temp == target:
                return [sort_idx_list[i], sort_idx_list[left], sort_idx_list[right]]
            elif temp < target:
                left += 1
            else:
                right -= 1
    return []
