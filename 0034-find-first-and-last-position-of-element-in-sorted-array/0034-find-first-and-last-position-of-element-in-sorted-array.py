class Solution(object):
    def searchRange(self, nums, target):

        #First occurence:
        def findFirst(nums,target):
            low = 0
            high = len(nums)-1 
            first = -1
            while low <= high:
                mid = low + (high-low)//2
                if target == nums[mid]:
                    first = mid
                    high = mid -1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid -1
            return first
        #Last occurence
        def findSecond(nums,target):
            low = 0
            high = len(nums)-1 
            second = -1
            while low <= high:
                mid = low + (high-low)//2
                if target == nums[mid]:
                    second = mid
                    low = mid + 1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid -1
            return second

        first = findFirst(nums, target)
        second = findSecond(nums,target)
        
        return [first, second]
            
        