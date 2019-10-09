class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                l = i + 1
                r = len(nums)-1
                
                while l < r:
                    sum  = nums[i] + nums[l] + nums[r]
                    if sum == 0:
                        results.append([nums[i], nums[l],nums[r]])
                        l += 1
                        r -= 1
                        
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums [r+1]:
                            r -= 1
                    elif sum > 0:
                        r -= 1
                    else:
                        l += 1
        return results

        
