"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        if y > x:
            x , y = y, x
        bin_x = str(bin(x)[2:])
        bin_y = str(bin(y)[2:])
        
        count = 0
        
        # fill the front with 0
        for i in range(len(bin_x)-len(bin_y)):
            bin_y = '0'+ bin_y
        
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                count += 1
        return count
