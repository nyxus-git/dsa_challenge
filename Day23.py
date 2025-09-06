from collections import deque

def sliding_window_maximum(arr, k):
   if not arr or k <= 0:
       return []
   
   dq = deque()
   result = []
   
   for i in range(len(arr)):
       while dq and arr[i] > arr[dq[-1]]:
           dq.pop()
       
       while dq and dq[0] <= i - k:
           dq.popleft()
       
       dq.append(i)
       
       if i >= k - 1:
           result.append(arr[dq[0]])
   
   return result

arr = [1, 5, 3, 2, 4, 6]
k = 3
print(sliding_window_maximum(arr,k))
