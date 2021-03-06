'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
    Input: [1,2,3]
    Output: 6
Example 2:
    Input: [1,2,3,4]
    Output: 24
Note:
    1. The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    2. Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1,max2,max3,min1,min2=-1000,-1000,-1000,0,0
        for i in nums:
            if i>max3:
                if i<=max2:
                    max3=i
                else:
                    if i<=max1:
                        max3=max2
                        max2=i
                    else:
                        max3=max2
                        max2=max1
                        max1=i
            if i<min2:
                if i>=min1:
                    min2=i
                else:
                    min2=min1
                    min1=i
        if max2*max3<min1*min2:
            return max1*min1*min2
        else:
            return max1*max2*max3