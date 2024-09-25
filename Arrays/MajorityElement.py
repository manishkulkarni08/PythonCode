#approach 1
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

#approach 2
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

#approach 3
def majority_element_moore(array:list)->int:
    cnt = 0
    majority_cnt = 0
    element = None

    for i in range(len(array)):
        if cnt ==0:
            cnt=1
            element =array[i]

        elif array[i]==element:
            cnt+=1
        else:
            cnt-=1

    for i in range(len(array)):
        if array[i]==element:
            majority_cnt+=1
    if majority_cnt>len(array)/2:
        return element
    return -1


majority_element([2,2,1,3,2,2])
print(majority_element_dict([2,2,1,3,2,2]))
print(majority_element_moore([2,2,1,3,2,2,1,1,1,2,2]))
