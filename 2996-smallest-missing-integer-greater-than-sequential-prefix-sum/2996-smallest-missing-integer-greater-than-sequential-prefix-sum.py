class Solution(object):
    def missingInteger(self, nums):
        if len(nums) < 2:
            return nums[0]+1
        start = nums[0]
        res = 0
        i = 0
        while i < len(nums):
            if nums[i] == start + i:
                res += nums[i]
                i += 1
                continue
            else:
                if res not in nums:
                    return res 
                else:
                    res += 1  
        return res


                
                
                    
        