# create a pascal triangle given number of rows


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # initialize the first row of triangle
        if numRows == 0:
            return []
        ans = [[1]]
        for n in range(1,numRows):
            print(n)
            ans.append([])
            for j in range(0,n+1):
                if j != 0 and j != (n):
                    ans[n].append(ans[n-1][j-1]+ans[n-1][j])
                else:
                    ans[n].append(1)
        return ans
