class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dictDuplicates= {}
        for i in range(len(nums)):
            if dictDuplicates.__contains__(nums[i]) and i-dictDuplicates.get(nums[i])  <= k:
                return True
            else:
                dictDuplicates.__setitem__(nums[i], i)
        return False
        