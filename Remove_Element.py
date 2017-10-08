class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums[0] == val:
            nums.pop(0)
        else:
            pass

        self.removeElement(nums[1:], val)

        return nums

    def removeElementRec(self, nums, val):
        


print (Solution().removeElement([3,2,2,3], 3))
