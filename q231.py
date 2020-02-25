class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(n >= 0):
            if n == 1:
                return True
            elif n % 2 == 1:
                return False
            elif n < 1 :
                return False
            else:
                n = n / 2
            print(n)
        return False