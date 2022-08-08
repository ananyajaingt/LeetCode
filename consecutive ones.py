class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        self.nums = nums

        c = 0
        maxc= 0

        for i in nums:
            if i == 1:
                c += 1
                maxc = max(c,maxc)

            else:
                c = 0

        return maxc

ob1 = Solution()
result1 = ob1.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
print(result1)