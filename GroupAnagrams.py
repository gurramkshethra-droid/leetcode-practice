class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans={}
        for s in strs:
            key="".join(sorted(s))
            if key not in ans:
                ans[key]=[]
            ans[key].append(s)
        return list(ans.values())

