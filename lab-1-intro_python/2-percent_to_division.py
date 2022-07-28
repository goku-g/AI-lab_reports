distic = 80
first = 60
second = 55
third = 40

percent = float(input("Enter percentage: "))

if(percent >= distic):
    print("You got distiction.")

elif(percent >= first):
    print("You got first division.")

elif(percent >= second):
    print("You got second division.")

elif(percent >= third):
    print("You got third division.")

elif(percent < third):
    print("You failed.")