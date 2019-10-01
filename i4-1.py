class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # loop through the whole list
        # check if it's always increasing
        # once it's not increasing, check if it's only decreasing
        
        inc = 1
        dec = 0
        val = 0
        for i in range(1,len(A)):
            if (inc == 1 and dec == 0):
                if (A[i] <= A[i-1]):
                    val = i-1
                    inc = 0
                    dec = 1
            elif (inc == 0 and dec == 1):
                if (A[i] >= A[i-1]):
                    return 0
        return val
            
            
