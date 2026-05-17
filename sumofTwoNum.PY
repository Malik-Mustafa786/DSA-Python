nums = [2, 3, 4, 5]
target = 8

dic = {}


for i, num in enumerate(nums):
  diff = target - num
  if diff in dic:
    print([dic[diff], i])

  dic[num] = i