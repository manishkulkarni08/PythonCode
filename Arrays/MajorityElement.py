def majority_element(array:list)->int:
    
    max_element_count = int(len(array)/2) 

    for i in range(len(array)):
        count =0

        for j in range(len(array)):
            if array[i] == array[j]:
                count+=1
        
        if count>=max_element_count:
            print(array[i])
            break
    else:
        print("No element")

def majority_element_dict(array:list)->int:
    dct =dict()
    for i in range(len(array)):
        if array[i] in dct:
            dct[array[i]]+=1
        else:
            dct[array[i]]= 1

    max_val = max(zip(dct.values(),dct.keys()))
    if max_val[0] >= int(len(array)/2) :
        return max_val[1]
    else:
        return -1

majority_element([2,2,1,3,2,2])
print(majority_element_dict([2,2,1,3,2,2]))
