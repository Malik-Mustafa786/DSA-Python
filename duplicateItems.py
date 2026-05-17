nums = [1, 2, 3, 4, 2, 1]
set = set()

for i in nums:
  if i in set:
    print(True)
    break
  set.add(i)
else:
  print(False)