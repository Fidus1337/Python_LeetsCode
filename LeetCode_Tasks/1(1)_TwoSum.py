"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution(object):
    """The class for solution"""

    def twoSum(self, nums, target):
        # first number of pair
        for first_index, first_number in enumerate(nums):
            # second number of pair
            for second_index, second_number in enumerate(nums):
                if first_index == second_index:  # we check if it is not the same number in pair
                    continue
                if first_number + second_number == target:
                    return [first_index, second_index]
                else:
                    continue
        return None

    def twoSum2(self, nums, target):
        mapping = {}
        # first number of pair
        for first_index, first_number in enumerate(nums):
            complement = target - first_number
            if complement in mapping:
                return [first_index, mapping[complement]]
            else:
                mapping[first_number] = first_index
        return None

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums)):
            if target-nums[i] in nums and nums.index(target - nums[i]) != i:
                res.append(i)
                res.append(nums.index(target - nums[i]))
                return res


test = Solution()
print(test.twoSum3([2, 11, 15, 250, 8, 9, 7], 9))
