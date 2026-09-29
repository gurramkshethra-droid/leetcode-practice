class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        mm=float('-inf')
        l=0
        for k in d:
            if mm<d[k]:
                mm=d[k]
                l=k
        return l
