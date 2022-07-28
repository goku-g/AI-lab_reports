
def pattern(num):
    for i in range(num):
        for j in range(i+1):
            print(j+1,end='\t')
        print("")

    print("----------------------------------")
    for i in range(num):
        for j in range(i+1):
            print(i+1,end='\t')
        print("")

var = int(input("How many pattern you want to print: "))
pattern(var)