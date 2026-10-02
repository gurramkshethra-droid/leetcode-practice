class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a=bin(x)[2:]
        b=bin(y)[2:]
        while len(a)<len(b):
            a="0"+a
        while len(b)<len(a):
            b="0"+b
        cnt=0
        for i,j in zip(a,b):
            if i!=j:
                cnt+=1
        return cnt
