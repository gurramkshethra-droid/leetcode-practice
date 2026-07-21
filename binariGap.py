class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=bin(n)[2:]
        ans=0
        last=-1
        for i in range(len(s)):
            if s[i]=='1':
                if last!=-1:
                    ans=max(ans,i-last)
                last=i
        return ans
