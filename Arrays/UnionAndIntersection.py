def union_set(array1:list,array2:list)->list:
    i,j=0,0
    union =list()
    while (i<len(array1) and j <len(array2)):
        if array1[i] <=  array2[j]:
            if array1[i] not in union:
                union.append(array1[i])
            i+=1

        elif array1[i] >  array2[j]:
            if array2[j] not in union:
                union.append(array2[j])
            j+=1

        if i==len(array1) and j!= len(array2):
            for k in range(j,len(array2)):
                union.append(array2[k])
        

        if j==len(array2) and i!= len(array1):
            for k in range(i,len(array2)):
                union.append(array1[k])
    return union
            
print(union_set([1,2,3],[1,2,4,5,6]))