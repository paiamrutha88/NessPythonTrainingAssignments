number = 28
sum =0

for i in range(1,number):
    if(number%i==0):
        sum=sum+i

if(sum==number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")



