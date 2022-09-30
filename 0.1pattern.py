n=int(input("ENTER THE NUMBER OF ROWS---> "))
for i in range(1,n+1):
    k=0.1
    for j in range(1,i+1):
        print("%.1f"%k,end=" ")
        k=k+0.1
    print("\n")
