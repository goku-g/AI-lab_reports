def calculate(a, b):
    return a+b, a-b, a*b, a/b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum, diff, product, quatient = calculate(num1, num2)

print("Sum = ", sum, "\nDifference = ", diff, "\nProduct = ", product, "\nQuatient = ", quatient)