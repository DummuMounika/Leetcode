class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        dictArr1 = {}
        for arr in arr1:
            if not arr in dictArr1:
                dictArr1[arr] = 1
            else:
                val = 1
                dictArr1[arr] += val

        result = []
        for num in arr2:
            if num in dictArr1:
                result.extend([num] * dictArr1[num])
                del dictArr1[num]

        sortTheRemaining = sorted(dictArr1.keys())
        for num in sortTheRemaining:
            result.extend([num]*dictArr1[num])
        return result




        



        