def find_the_duplicate_number(numbers_array):
    slow_mover = numbers_array[0]
    fast_mover = numbers_array[numbers_array[0]]

    while slow_mover != fast_mover:
        slow_mover = numbers_array[slow_mover]
        fast_mover = numbers_array[numbers_array[fast_mover]]
    start_pointer = 0

    while start_pointer != slow_mover:
        start_pointer = numbers_array[start_pointer]
        slow_mover = numbers_array[slow_mover]

    return start_pointer
my_array = [1,4,4,2,3]
duplicate = find_the_duplicate_number(my_array)
print(f"The duplicate number is: {duplicate}")
