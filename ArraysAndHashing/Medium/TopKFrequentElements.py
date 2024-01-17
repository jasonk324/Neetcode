class Solution(object):
    def topKFrequent(self, nums, k):
        counter_dict = dict()
        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 0
            else:
                counter_dict[num] += 1
        counter_list = sorted(counter_dict, key=lambda x: counter_dict[x], reverse=True)

        return counter_list[:k]