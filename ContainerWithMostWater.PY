class Solution:

    def maxWater(self, hieght: list[int]) -> int:
        #   BRUCE FORCE APPROACH
        #   res = 0

        #   for l in range(len(hieght)):
        #     for r in range(l + 1, len(hieght)):
        #       area = (r - l) * min(hieght[l], hieght[r])
        #       res = max(res, area)
        #   return res
        res = 0
        l, r = 0, len(hieght) - 1
        while l < r:
            area = (r - l) * min(hieght[l], hieght[r])
            res = max(res, area)
            if hieght[l] < hieght[r]:
                l += 1
            else:
                r -= 1
        return res


sol = Solution()
obj = sol.maxWater([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(obj)
