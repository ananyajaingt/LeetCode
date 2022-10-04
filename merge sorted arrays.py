class Solution(object):
    def merge(self, nums1, m, nums2, n):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n

        nums1 = nums1[0:m]

        for i in range(m, m + n):
            nums1.append(0)

        nums1[m:m + n] = nums2[0:n]

        nums1.sort()
        print(nums1)

ob1 = Solution()
ob_merge = ob1.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
