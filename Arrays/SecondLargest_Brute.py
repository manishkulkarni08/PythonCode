#O(2N)
import sys

a = [1,3,5,4,7,3,2,7]

largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
print("Largest ",largest)

second_largest = -sys.maxsize
for i in range(len(a)):
    if a[i] > second_largest and a[i] !=largest:
        second_largest = a[i]


print("Second Largest ",second_largest)
