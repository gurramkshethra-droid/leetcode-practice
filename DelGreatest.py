class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum=0
        maxm=0
        for j in range(len(grid[0])):
            maxm=0
            for i in grid:
                s=max(i)
                i.remove(s)
                maxm=max(maxm,s)
            sum+=maxm
        return sum
