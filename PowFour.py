class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans=1
        while ans<n:
            ans*=4
        return ans==n
