class Solution(object):
    def twoSum(self, nums, target):
        res=0
        dictsum= {}
        for i in range(len(nums)):
            res = target - nums[i]
            if dictsum.__contains__(res):
                return [dictsum.get(res),i]
            else:
                dictsum.__setitem__(nums[i], i)
        