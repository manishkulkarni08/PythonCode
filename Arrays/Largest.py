a = [1,3,5,4,3,2]

largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]


print(largest)