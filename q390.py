class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = list(range(1,n+1))
        flip = 1
        
#         this is accurate but time limit exceeded
        while(len(l)>1):
            if (flip == 1):
                toD = []
                for i in range(0,len(l)):
                    if (i%2 == 0):
                        toD.append(l[i])
                for i in range(len(toD)):
                    l.remove(toD[i])
                
            else:
                toD = []
                for i in range(len(l)):
                    if ((i+1)%2 == 1):
                        toD.append(l[-(i+1)])
                for i in range(len(toD)):
                    l.remove(toD[i])
            flip = flip*(-1)
        return l.pop()