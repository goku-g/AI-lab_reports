
def bubble_sort(array):
    l = len(array)

    for i in range(l-1):
        t_len = len(array[i:l-1])
        for j in range(t_len):
            if array[j] >= array[j + 1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
                # array[j],array[j+1] = array[j+1], array[j]
    return array

array = [5, 99, 11, 13, 51]
array = bubble_sort(array)
print(array)

# alternatively:
# array.sort()
# print(array)