class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=0
        for i in digits:
            n=n*10+i
        n+=1
        n=str(n)
        t=[]
        for i in n:
            t.append(int(i))
        return t
