class Solution(object):
    def numberOfSubarrays(self, nums, k):
        left = 0
        right = 0
        oddn = 0
        countOfSubarrays = 0
        res = 0
        while right < len(nums):
            if nums[right] %2 != 0:
                oddn += 1
                countOfSubarrays = 0
            
            while oddn == k:
                if nums[left] %2 != 0:
                    oddn -= 1
                countOfSubarrays += 1
                left += 1
            right += 1

            res += countOfSubarrays
            
        return res


