import sys
def second_largest(array:list) ->int:
    largest_element = array[0]
    second_largest = - sys.maxsize -1

    for i in range(1,len(array)):
        if array[i] > largest_element:
            second_largest,largest_element =largest_element,array[i]
        elif array[i] < largest_element and array[i] >second_largest :
            second_largest = array[i]
    return second_largest

array = [1,3,5,4,7]
print("Second Largest",second_largest(array))


def second_smallest(array:list)-> int:
    smallest = array[0]
    s_smallest = sys.maxsize -1

    for i in range(1,len(array)):
        if  array [i] < smallest:
            s_smallest= smallest 
            smallest = array[i]
        elif  array[i] != smallest and  array[i] < s_smallest :
            s_smallest = array[i]
    return s_smallest

print("Second smallest",second_smallest(array))

