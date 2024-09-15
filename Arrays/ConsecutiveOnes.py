def consecutive_ones(array:list)->int:
    max_one,count =0,0 
    for i in range(len(array)):
        if array[i]==1:
            count+=1
        elif array[i]!=1:
            count=0

        if count >= max_one:
            max_one = count
    return max_one


print(consecutive_ones([1,1,0,0,1,1,1,1,0,1]))