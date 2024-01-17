class Solution(object):
    def twoSum(self, numbers, target):
        left_pointer = 0
        right_pointer = len(numbers) - 1
        sum = None

        while sum != target:
            sum = numbers[left_pointer] + numbers[right_pointer]
            if sum == target:
                print(left_pointer)
                print(right_pointer)
                return [left_pointer + 1, right_pointer + 1]
            else:
                if sum > target:
                    right_pointer -= 1
                else:
                    left_pointer += 1

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        