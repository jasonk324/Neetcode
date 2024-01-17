class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        final_list = list() 

        for i, num in enumerate(nums):
            # Only a negative number can bring it to 0
            if num > 0:
                break

            # Skip if the same value repeat
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = num + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    final_list.append([num, nums[l], nums[r]])
                    l += 1
                    # BE AWARE OF THIS PART BC THIS IS WHAT YOU KEPT FORGETTING
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return final_list
