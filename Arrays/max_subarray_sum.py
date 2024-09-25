
def max_sub_array_sum(array:list)->int:
    max_val = -999999999
    sum = 0

    for i in range(len(array)):
        if array[i] > max_val:
            max_val = array[i]

        sum+= array[i]

        if sum > max_val:
            max_val = sum
        
        if sum <0:
            sum=0
        
    return max_val


print(max_sub_array_sum([-2,-3,4,-1,-2,1,5,-3]))
print(max_sub_array_sum([-2,-3,-4,-1]))