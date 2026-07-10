class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cs="1"
        for i in range(n-1):
            count=1
            temp=""
            if cs=="1":
                cs="11"
                continue
            for j in range(len(cs)-1):
                if cs[j]==cs[j+1]:
                    count+=1
                else:
                    temp+=str(count)+cs[j]
                    count=1
            temp+=str(count)+cs[-1]
            cs=temp
        return cs

        
