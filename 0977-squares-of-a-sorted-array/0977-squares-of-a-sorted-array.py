class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n= len(nums)
        res = [0] * n
        l = 0
        r = n-1
        index = n-1
        while l <= r:
            leftsq = nums[l]*nums[l]
            rightsq = nums[r]*nums[r]

            if leftsq > rightsq:
                res[index] = leftsq
                l += 1
            else:
                res[index] = rightsq
                r -= 1

            index -=1
        return res

        