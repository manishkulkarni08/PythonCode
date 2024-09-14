a = [1,1,1,2,2,3,3,4,4,4,5]
print(a)
i = 0
for j in range(1,len(a)):
    if a[i] != a[j]:
        a[i+1] = a[j]
        i+=1

print(i+1)

        
