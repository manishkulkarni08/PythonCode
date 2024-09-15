def moveall_0_to_end(array:list)->list:
    temp_0 =list()
    temp_rest = list()
    for i in range(len(array)):
       if array[i]==0:
        temp_0.append(array[i])
       else:
         temp_rest.append(array[i])

    return temp_rest+ temp_0


#print(moveall_0_to_end([1,2,0,0,3,0,5,6,0]))
     
#2nd approach
def moveall_0_to_end_ap2(array:list)->list:  
   count = 0 
   for i in range(len(array)):
      if array[i] !=0:
         array[count] = array[i]
         count+=1
    
   while count < len(array):
      array[count]=0
    
   return array

print(moveall_0_to_end_ap2([1,2,0,0,3,0,5,6,0]))


      
