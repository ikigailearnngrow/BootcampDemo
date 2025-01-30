for i in range(1, 5 + 1):
        # Print leading spaces
        p=1
        for j in range(5 - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print(p, end="")
            p=p+1
        print()
