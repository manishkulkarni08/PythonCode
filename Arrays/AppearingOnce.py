def find_appearing_once(array:list)->int:
    xor = 0
    for i in range(len(array)):
        xor = xor ^ array[i]

    return xor 

print(find_appearing_once([1,1,2,2,3,4,4,5,5]))