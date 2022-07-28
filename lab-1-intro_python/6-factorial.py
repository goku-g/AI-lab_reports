
def fact_recur(a):
    if(a == 0 or a == 1):
        return 1
    prod = a * fact_recur(a-1)
    return prod

def fact_iterative(a):
    mul = 1
    if(a == 0 or a == 1):
        return 1
    for i in range(1,a+1):
        mul = mul*i
    return mul

num = int(input("Enter number: "))

factorial = fact_recur(num)
print("Factorial is {}".format(factorial))

factorial = fact_iterative(num)
print("Factorial is {}".format(factorial))