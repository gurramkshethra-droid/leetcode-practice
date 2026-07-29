class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        for i in range(32):
            bit=n%2
            ans=ans*2+bit
            n//=2
        return ans
