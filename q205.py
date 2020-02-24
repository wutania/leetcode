class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        if s == '' or t == '':
            return False
        if len(s) != len(t):
            return False
        d_S = {}
        d_T = {}
        for i in range(len(s)):
            if s[i] in d_S and t[i] in d_T:
                if d_S[s[i]] != d_T[t[i]]:   # if the last time we see this char is different then the order has changed
                    return False
            elif (s[i] in d_S and t[i] not in d_T) or (s[i] not in d_S and t[i] in d_T): 
                return False 
            d_S[s[i]] = i
            d_T[t[i]] = i   # track the last time we see this char
        return True
