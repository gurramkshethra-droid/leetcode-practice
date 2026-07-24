class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxm=0
        for l1 in accounts:
            s=sum(l1)
            if maxm<s:
                maxm=s
        return maxm
