class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print (nums)
        count = 0
        for i in range(len(nums)-1):
            print("nums[i]= ", nums[i])
            if (nums[i] != nums[i+1]):
                if (count != 1):
                    return nums[i]
                else:
                    count = 0
            else:
                count += 1
        return nums[-1]
