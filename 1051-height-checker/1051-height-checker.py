class Solution(object):
    def heightChecker(self, heights):
        expectedH = sorted(heights)
        countVary = 0
        for i in range(len(heights)):
            if heights[i] != expectedH[i]:
                countVary += 1
        return countVary





        