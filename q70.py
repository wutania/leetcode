import math 
class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            if (float((n-i)/2).is_integer()):
                if (i == 0 or (n-i)/2 == 0):
                    count += 1
                else:
                    count += int((math.factorial(i + (n-i)/2)/(math.factorial(i)*math.factorial((n-i)/2))))
        return count
