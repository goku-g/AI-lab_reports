st_info = {}
num = int(input("How many student over there?\n"))

for i in range(num):
    name = input("Enter student Name: ")
    st_info[name] = input("Enter student Mark: ")

print("SN \t| Name \t\t\t\t| Mark")
print("----------------------------------------------")
i = 1
for key in st_info.keys():
    print("{} \t| {} \t\t| {}".format(i, key.upper(), st_info[key]))
    i = i + 1