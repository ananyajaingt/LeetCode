class Solution(object):
    def duplicateZeros(self, arr):
        self.arr = arr

        d = 0
        l = len(arr) - 1

        for i in range(len(arr)):
            if i > l - d:
                break

            if arr[i] == 0:
                if i == l - d:
                    arr[l] = 0
                    l -= 1
                    break
                d += 1

        last = l - d

        for j in range(last, -1, -1):
            if arr[j] == 0:
                arr[j + d] = 0
                d -= 1
                arr[j + d] = 0
            else:
                arr[j + d] = arr[j]

        print(arr)


ob1 = Solution()
ob_zero = ob1.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
