from numpy import append

def list_prime(num_list):
    prime = []

    for i in num_list:
        factors = 0
        # print(i)
        if(i == 1):
            pass

        elif(i == 2):
            prime.append(i)
        
        else:
            for j in range(2,i+1):
                temp = str(i/j)
                dec = temp.split(".")[1]

                if int(dec) == 0:
                    factors += 1
        
            if(factors <= 1):
                prime.append(i)
    return prime

num_list = range(1, 101)
prime = list_prime(num_list)
print(prime)