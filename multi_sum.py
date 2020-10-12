"""
@Author: ZHANG Mofan
@Time: 09/29/2020 22:00-23:00
"""


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

    nums.sort()
    len1 = len(nums)
    res = []
    if len1 <= 2:
        print(res)
    for i in range(len1 - 1):
        left, right = i + 1, len1 - 1  # inspired by quick sort
        while left < right:
            temp = nums[i] + nums[left] + nums[right]
            if temp == target and [nums[i], nums[left], nums[right]] not in res:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif temp < target:
                left += 1
            else:
                right -= 1

    return res
