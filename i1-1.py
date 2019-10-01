class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if (stones == []): # no stones
            return 0
        if (len(stones) == 1):
            return stones[0]
        
        stones.sort()
        a = stones[-2]
        b = stones[-1]
        k = self.smash(a, b)
        if (k == 0):
            return(self.lastStoneWeight(stones[0:-2]))
        else:
            stones = stones[0:-1]
            stones[-1] = k
            return(self.lastStoneWeight(stones))
        
    def smash(self, a, b):
        return b-a
