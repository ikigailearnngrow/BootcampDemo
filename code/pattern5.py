m=6
for i in range(1,(m//2+1)):
    for j in range(1,m):
        if(i==1 or (i==j or (i+j)==m)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
