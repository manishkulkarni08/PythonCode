def check_array_sorted(array:list)->bool:
    current_element = array[0]
    for i in range(1,len(array)):
        if current_element <= array[i]:
            current_element = array[i]
        else:
            return False
        
    return True

array = [1,2,2,3,3,5,6,8]
print(check_array_sorted(array))

array = [1,2,2,3,3,7,5,6,8]
print(check_array_sorted(array))