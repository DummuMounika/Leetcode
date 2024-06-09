class Solution(object):
    def subarraysDivByK(self, nums, k):
        dictNums = {0:1}
        sum = 0
        totalSubarray = 0
        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k
            if rem in dictNums:
                totalSubarray += dictNums[rem]
                dictNums[rem] += 1
            else:
                dictNums[rem] = 1
        return totalSubarray
        



        