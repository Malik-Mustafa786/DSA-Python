nums = [5, 4, -1, 7, 8]


def maxSubArray(nums):
    max_current = nums[0]
    max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[1], max_current + nums[i])
        max_global = max(max_global, max_current)
    return max_global


print(maxSubArray(nums))
