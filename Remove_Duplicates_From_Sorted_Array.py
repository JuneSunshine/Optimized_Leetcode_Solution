class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        p1, p2 = 0, 0

        while p2 < n and nums:

            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]


            p2 += 1

        return p1 + 1

print (Solution().removeDuplicates([1,1,1,3]))