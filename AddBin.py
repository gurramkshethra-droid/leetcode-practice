class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        i=len(a)-1
        j=len(b)-1
        ans=""
        while i>=0 or j>=0 or carry:
            s=carry
            if i>=0:
                s+=int(a[i])
                i-=1
            if j>=0:
                s+=int(b[j])
                j-=1
            ans=str(s%2)+ans
            carry=s//2
        return ans
            
        
