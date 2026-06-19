class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n=[0]
        s=0
        for i in gain:
            s+=i
            n.append(s)
        return max(n)
        
