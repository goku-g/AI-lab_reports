array = [88, 99, 77, 13, 51]
l = len(array)

for j in range(l-1):
    if array[j] >= array[j + 1]:
        temp = array[j + 1]
        array[j + 1] = array[j]
        array[j] = temp

print(array[-1])