class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if digits == []:
            return 
        y = (list(str(int("".join(map(lambda x: str(x),digits)))+1)))
        for i in range(len(y)):
            y[i] = int(y[i])
            
        return y