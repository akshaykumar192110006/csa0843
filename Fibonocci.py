n=int(input("enter the number of rows to be generated:"))
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()
