class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        # map(str,A) makes the whole list into str from int
        # join the list to a sring
        # make it back to integer to do addition
        # then split it back into list of int via int(d) for d in str())
        return [int(d) for d in str(int(''.join(map(str, A))) + K)]


