#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#Example:

#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # if nums is empty return 0
        if nums == []:
            return 0
        if len(nums) == 1:
            
        
        # create new array of sub arrays called subArrays
        subArrays = []
        
        # trying to loop through all the sub arrays
        # eg. 0, 01, 012, 0123...012345678, 1, 12, 123, ... 12345678, 2, 23, 234,
        # the way to do so is loop through the entire list
        for i in range(len(nums)-1):
            ans = 0
            carry = nums[i]
            # incl the prev number (or sum of numbers) as carry
            for j in range(i+1, len(nums)):
                ans = ans + carry
                subArrays.append(ans)
                carry = nums[j]
        subArrays.append(nums[-1])
        return max(subArrays)


