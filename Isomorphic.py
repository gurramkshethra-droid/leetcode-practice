class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}
        flag=True
        for i,j in zip(s,t):
            if i not in d:
                if j in d.values():
                    flag=False
                    break
                d[i]=j
            else:
                if d[i]!=j:
                    flag=False
                    break
        return flag
