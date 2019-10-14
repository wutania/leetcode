#Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        return combinations(range(1,n+1), k)
