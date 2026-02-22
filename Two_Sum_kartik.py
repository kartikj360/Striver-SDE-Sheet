class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,value in enumerate(nums):
            for next_index,value2 in enumerate(nums[index+1:],start=index+1):
                if (value+value2==target):
                    return [index,next_index]
                    break
        return []