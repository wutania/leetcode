class Solution(object):
    
    # find the first next non - zero index
    def swapZero(self, nums, i):
        for j in range(i, len(nums)):
            if nums[j] != 0:
                return j
        return -1
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                # find the closest non-zero num's index
                j = self.swapZero(nums, i)
                #swap
                if (j == -1):
                    break
                nums[i],nums[j] = nums[j],nums[i]
                
        # a faster method is to append a zero and remove the current zero but i didn't know i can modify the length of the array 
        # n=len(nums)
        # i=0
        # while i < n:            
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #         n-=1   # number of non-zeros modified
        #     else:    
        #         i+=1