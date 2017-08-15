class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        usedChars = {}
        max_len, start = 0, 0

        for index, value in enumerate(s):
            if value in usedChars and start <= usedChars[value]:
                start = usedChars[value] + 1
            else:
                max_len = max(max_len, 1 + index - start)
            usedChars[value] = index
        return max_len