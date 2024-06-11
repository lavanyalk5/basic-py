n=14
if (n==0 and n==1):
    print("Not Prime")

elif(n>=2):
    for i in range (2,10):
        if(n%i==0):
            print(" Prime")
            print(n)
            exit()
        print("not Prime")