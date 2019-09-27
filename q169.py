class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = {}
        max = 0
        numMax = 0
    
        for i in range(len(nums)):
            if (nums[i] not in numDict):
                numDict[nums[i]] = 1
            elif (nums[i] in numDict):
                numDict[nums[i]] = numDict.get(nums[i]) + 1

            if (numDict[nums[i]] > max):
                max = numDict[nums[i]]
                numMax = nums[i]
        return numMax
    
    
    
