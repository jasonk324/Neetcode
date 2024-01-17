class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            length = 0 
            if num + 1 not in num_set:
                while num in num_set:
                    num -= 1
                    length += 1
            longest = max(longest, length)
    
        return longest

        """
        :type nums: List[int]
        :rtype: int
        """
        