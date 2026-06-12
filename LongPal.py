class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                st = s[i:j+1]

                if st == st[::-1]:
                    if len(st) > len(longest):
                        longest = st

        return longest