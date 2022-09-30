n=int(input("ENTER NUMBER OF ELEMENTS---> "))
arr=[]
for i in range(0,n):
    a=input("ENTER THE ELEMENTS---> ")
    arr.append(a)
print(arr)
ch=input("ENTER THE ORDER RQUIRED(A/D)----> ")
if(ch=='A' or ch=='a'):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("ascending order")
    for i in range(0,n):
        print(arr[i])
elif(ch=='D' or ch=='d'):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]<arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("descending order")
    for i in range(0,n):
        print(arr[i])
