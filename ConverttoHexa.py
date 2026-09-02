class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        if num<0:
            num=num&0xffffffff
        hexs="0123456789abcdef"
        result=""
        while num>0:
            rem=num%16
            result=hexs[rem]+result
            num//=16
        return result
