class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        for i in range(len(nums)):
            s.append(nums[nums[i]])
        return s
        
