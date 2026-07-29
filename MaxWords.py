class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        cnt=0
        for i in sentences:
            t=i.split(" ")
            cnt=max(cnt,len(t))
        return cnt
