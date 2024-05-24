class Solution(object):
    def longestOnes(self, nums, k):
        zerocount = 0
        start = 0
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zerocount += 1

            while zerocount > k :
                if nums[start] == 0:
                    zerocount -= 1
                start += 1

            leng = i - start + 1
            if max_ones < leng:
                max_ones = leng
        return max_ones




        
        