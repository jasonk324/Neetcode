class Solution(object):
    def productExceptSelf(self, nums):

        num_list = [1] * len(nums)

        left_product = 1
        for i in range(0, len(nums)):
            num_list[i] *= left_product 
            left_product *= nums[i]

        print(num_list)
        
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            num_list[i] *= right_product
            right_product *= nums[i]


        print(num_list)

        return num_list
    
# Create an instance of the Solution class
solution_instance = Solution()

# Example input list
nums = [1, 2, 3, 4]

# Call the productExceptSelf method
solution_instance.productExceptSelf(nums)
