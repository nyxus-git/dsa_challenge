def Find_Leaders(arr):
    n = len(arr)
    leaders = []
    max_Right = arr[n-1]
    leaders.append(max_Right) 

    for i in range(n-2, -1, -1):  
        if arr[i] > max_Right:
            maxFromRight = arr[i]
            leaders.append(arr[i])

    leaders.reverse()
    return leaders

arr = [5]
print(Find_Leaders(arr))
