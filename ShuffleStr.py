class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        l=[""]*len(s)
        for i in range(len(s)):
            l[indices[i]]=s[i]
        st=""
        for i in l:
            st+=i
        return st

        
