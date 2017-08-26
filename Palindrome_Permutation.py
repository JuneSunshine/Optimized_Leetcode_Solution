class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        d = {}
        for ss in s:
            if ss not in d.keys():
                count = s.count(ss)
                d[ss] = count
        li = list(d.values())
        counts = [x % 2 for x in li]
        return sum(counts) < 2

a = Solution().canPermutePalindrome("aab")
print (a)