def findMissingValue(arr):
  size = len(arr)
  n = size + 1

  expected_sum = n * (n+1)/2

  present_sum = 0
  for num in arr:
    present_sum += num
  lost_number = expected_sum - present_sum
  return lost_number

arr = [1]
print(int(findMissingValue(arr)))
