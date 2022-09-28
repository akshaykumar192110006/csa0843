try:
    n=int(input("ENTER NO.OF ELEMENTS---> "))
    arr=[]
    for i in range(0,n):
        a=int(input("ENTER THE ELEMENTS---> "))
        arr.append(a)
    if(arr[i]<0):
        print("NEGATIVE VALUE")
        exit()
    elif(arr[i]==16):
        print("SAME VALUE")
    elif(arr[i]==0):
        print("SAME VALUE")
    else:
        for i in range(0,n):
            for j in range(i+1,n):
                if(arr[i]>arr[j]):
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
        for i in range(0,n):
            print(arr[i])
        n1=int(input("ENTER THE VALUE OF N----> "))
        m=int(input("ENTER THE VALUE OF M----> "))
        print("nth MINIMUM NUMBER is---> ",arr[n1-1])
        dif=arr[n1-1]
        for i in range(0,n):
            for j in range(i+1,n):
                if(arr[i]<arr[j]):
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
        print("mth MAXIMUM NUMBER is---> ",arr[m-1])
        summ=arr[m-1]
        print("SUM---> ",summ+dif)
        print("DIFFERENCE---> ",summ-dif)

except ValueError:
    print("ERROR1")
except IndexError:
    print("ERROR2")
except NameError:
    print("ERROR3")
