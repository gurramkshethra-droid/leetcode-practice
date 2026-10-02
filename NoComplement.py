class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        st=bin(num)[2:]
        n=""
        for i in st:
            if i=="1":
                n+="0"
            else:
                n+="1"
        return int(n,2)
