def findOccurance(arr, k):
  frequency_map = {}
  for element in arr:
    if element in frequency_map:
      frequency_map[element] += 1
    else:
      frequency_map[element] = 1
      
  for element in arr:
    if frequency_map[element] == k:
      return element

  return -1

arr =  [6, 6, 6, 6, 7, 7, 8, 8, 8]
k = 4
print(findOccurance(arr, k))
