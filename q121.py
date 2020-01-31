class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #max profit = buy low sell high
        #if array is always descending then you should never buy + sell 
        if prices == []:
            return 0
        maxP = 0
        minN = prices[0]
        for num in range(1,len(prices)):
            if prices[num] < minN:
                minN = prices[num]
            if prices[num] > minN:
                if prices[num] - minN > maxP:
                    maxP = prices[num]-minN
        return maxP