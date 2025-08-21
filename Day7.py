def trap_water(height):
    if len(height) < 3: return 0
    left = 0
    right = len(height) - 1
    left_max = right_max = total = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total += right_max - height[right]
            right -= 1
    return total

height =   [2, 0, 2]
print(trap_water(height))
