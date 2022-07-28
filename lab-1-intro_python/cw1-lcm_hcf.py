def gcd_and_lcm(num1, num2):
    a = num1
    b = num2
    if num2 == 0:
        return num1
    else:
        while(num2 != 0):
            r = num1 % num2
            num1 = num2
            num2 = r
    return num1, a*b/num1

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

lcm, hcf = gcd_and_lcm(x, y)

print("LCM: ", lcm)
print("HCF: ", hcf)