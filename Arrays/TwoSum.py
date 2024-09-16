def two_sum(array:list,sum:int)->bool:
    for i in range(len(array)):
        temp_sum =  sum - array[i]
        if temp_sum in array:
            return True
    return False


print(two_sum([2,4,6,5,8,11],16))

