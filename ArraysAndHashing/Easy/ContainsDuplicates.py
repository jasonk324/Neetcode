class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()
        
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False