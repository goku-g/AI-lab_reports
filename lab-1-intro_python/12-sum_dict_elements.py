dict_1 = {'a':100, 'b':200, 'c':500}
dict_2 = {'z':150, 'y':50, 'x':200}

def sum_dict(dict):
    sum = 0
    for key in dict:
        sum = sum + dict[key]
    return sum

sum = sum_dict(dict_1)
print("Sum of all items in dictionary is {}".format(sum))

sum = sum_dict(dict_2)
print("Sum of all items in dictionary is {}".format(sum))