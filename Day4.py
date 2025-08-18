import math
def  merge_array(arr1, arr2):
  m , n = len(arr1) , len(arr2)
  total_length = m + n
  gap = math.ceil((m + n) / 2)
  
  while gap > 0:
    i=0
    while i + gap < total_length:

      if i < m and i + gap < m:
        if arr1[i] > arr1[i + gap]:
          arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
      
      elif i < m and i + gap >= m:
        if arr1[i] > arr2[i + gap - m]:
          arr1[i],arr2[i + gap - m]= arr2[i + gap - m],arr1[i]
      
      else:
        if arr2[i - m] > arr2[i + gap - m]:
          arr2[i - m],arr2[i + gap - m] = arr2[i + gap - m],arr2[i - m]
      i = i + 1

    if gap == 1:
      gap = 0
    else:
      gap = math.ceil(gap/2)

  return arr1,arr2

arr1 = [1, 3, 8] 
arr2 = [4, 6, 10]
print(merge_array(arr1,arr2))
