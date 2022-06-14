
def fact(a):
    if(a == 0 or a == 1):
        return 1
    prod = a * fact(a-1)
    return prod

num = int(input("Enter number: "))

factorial = fact(num)
print("Factorial is {}".format(factorial))