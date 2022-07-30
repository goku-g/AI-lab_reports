val = int(input("How many numbers in the list: "))
list_val = []

for i in range(val):
    data = int(input("Enter {} number: ".format(i+1)))
    list_val.append(data)

summation = 0
for num in list_val:
    summation = summation + num

print(summation)

# alternatively:
# s = sum(list_val)
# print(s)