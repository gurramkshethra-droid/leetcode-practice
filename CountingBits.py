class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        for i in range(n+1):
            cnt=0
            while(i>0):
                cnt+=(i&1)
                i=i>>1
            l.append(cnt)
        return l
        
