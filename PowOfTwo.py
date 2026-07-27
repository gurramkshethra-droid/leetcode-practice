import math
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        for i in range(int(math.log(n,2))+1):
            if pow(2,i)==n:
                return True

        return False
