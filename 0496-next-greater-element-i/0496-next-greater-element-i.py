class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        DictnextGreaterElement = {}
        for i in range(len(nums2)-1,-1,-1):
            element = nums2[i]
            while len(stack) != 0 and stack[-1] <= element:
                stack.pop()
            if len(stack) == 0:
                DictnextGreaterElement[element] = -1
            else:
                DictnextGreaterElement[element] = stack[-1]
            stack.append(element)

        res = []
        for num in nums1:
            res.append(DictnextGreaterElement[num])
        return res




        