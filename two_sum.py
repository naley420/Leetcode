#1 #Array #Hash Table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for index, num in enumerate(nums):
        #     if target - num in nums[index + 1:]:
        #         return [index, nums[index + 1:].index(target - num) + index + 1]
        
        nMap = {}
        
        for i in range(len(nums)):
            tmp = target - nums[i]
            
            if tmp in nMap:
                return [nMap[tmp], i]
            nMap[nums[i]] = i
            
        return []
            