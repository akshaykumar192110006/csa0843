n=float(input("enter the starting number"))
r=int(input("no of rows:"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print("%.1f"%n,end=" ")
        n=n+0.1
    print("\n")
