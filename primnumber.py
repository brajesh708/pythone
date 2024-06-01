
# num = 2820
# To take input from the user
num = int(input("Enter a number: "))
# define a flag variable
flag = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
    # check if flag is True
    # if flag:
    #     print(num, "is not a prime number")
    # else:
    #     print(num, "is a prime number")
    #     # next program 
    # n=int(input("enter any number"))
    # while i<n:
    #     if n%i==0:
    #         count=count+1
    #         if count: 1+ ("not a prime numner") 
    #     elif n%i==0:
    #         else ()
    #         print(n)
            
            
            
            __name__
            
            
            