class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

        dictCount = {0:1}
        sum = 0
        total_subarrays = 0

        for num in nums:
            sum += num

            if sum - goal in dictCount:
                total_subarrays += dictCount[sum - goal]
            if sum in dictCount:
                dictCount[sum] += 1
            else:
                dictCount[sum] = 1

        return total_subarrays


                
                
