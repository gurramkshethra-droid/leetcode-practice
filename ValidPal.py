class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        st=""
        for ch in s:
            if ch.isalnum():
                st+=ch
        return st==st[::-1]
