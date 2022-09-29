m=int(input("Enter the M Value:"))
n=int(input("Enter the K Value:"))
k=int(input("Enter the K Value:"))
if(m>n or m<0 or n<0 or k<0 or m==n):
    print("invalid input")
else:
    for i in  range(m,n+1,k+1):
        print(i)
