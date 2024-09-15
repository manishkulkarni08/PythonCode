def rotate_array_d_place(array:list,d:int)->list:
    d =  d%len(array)
    return array[d:]+array[:d]
    
print(rotate_array_d_place([1,2,3,4,5],1))
#print(9%7)


