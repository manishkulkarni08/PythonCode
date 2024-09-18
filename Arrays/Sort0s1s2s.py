def sort_array_0_1_2(array:list)->list:
    cnt_0,cnt_1,cnt_2=0,0,0
    for i in range(len(array)):
        if array[i]==0:
            cnt_0+=1
        if array[i]==1:
            cnt_1+=1
        if array[i]==2:
            cnt_2+=1
    idx = 0
    for i in range(cnt_0):
        array[idx]=0
        idx+=1

    for i in range(cnt_1):
        array[idx] =1
        idx+=1

    for i in range(cnt_2):
        array[idx] =2
        idx+=1

    return array


def sort_array_0_1_2_dnf(array:list)->list:
    low,mid,high=0,0,len(array)-1

    while mid<=high:

        if array[mid]==0:
            array[low],array[mid]=array[mid],array[low]
            low+=1
            mid+=1
        elif array[mid]==1:
            mid+=1
        else:
            array[mid],array[high]=array[high],array[mid]
            high-=1
    return array




array = [1,2,1,0,0,0,0,1,2,0,2,0,1,0,1,2,0,1]
print(sort_array_0_1_2(array))   
print(sort_array_0_1_2_dnf(array))   