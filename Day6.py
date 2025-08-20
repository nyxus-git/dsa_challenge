from collections import defaultdict

def find_zero_sum_subarrays(arr):
    result = []                 
    prefix_sum = 0              
    sum_to_indices = defaultdict(list)  
    sum_to_indices[0].append(-1) 

    for i in range(len(arr)):
        prefix_sum += arr[i]     
        if prefix_sum in sum_to_indices:
            for j in sum_to_indices[prefix_sum]:
                start = j + 1
                end = i
                result.append((start, end))

        sum_to_indices[prefix_sum].append(i)

    return result

arr = [-3, 1, 2, -3, 4, 0]
print(find_zero_sum_subarrays(arr))
