arr = [88, 99, 77, 13, 51]
array = arr

print(array)
l = len(array)

for j in range(l-1):
    if array[j] >= array[j + 1]:
        temp = array[j + 1]
        array[j + 1] = array[j]
        array[j] = temp

print(array[-1])

# alternatively:
# largest = max(arr)
# print(largest)