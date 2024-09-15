def left_rotate_by_one_pos(array)->list:
    length = len(array)
    temp = array[0]

    for i in range(1,len(array)):
        array[i-1] = array[i]

    array[i] = temp
    return array


print(left_rotate_by_one_pos([1,2,3,4,5]))