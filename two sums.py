class Solution():
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def countPairs(self) -> object:
        count = 0
        n = len(self.nums)
        for j in range(0, n):
            for i in range(0, j):
                if self.nums[i] == self.nums[j] and (i * j) % self.k == 0:
                    count += 1
        print(count)


ex1 = Solution([3, 1, 2, 2, 2, 1, 3], 2)
ex1.countPairs()
