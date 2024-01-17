class Solution(object):
    def twoSum(self, nums, target):
        num_dict={}
        for index, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], index]
            else:
                num_dict[num] = index

class Solution(object):
    def twoSum(self, nums, target):
        nums_set = set(nums)

        for index, num in enumerate(nums):
            if target - num in nums_set:
                if index != nums.index(target - num):
                    return [index, nums.index(target - num)] 