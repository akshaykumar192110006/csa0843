def cs(n,start):
    if(n==0):
        return 1
    count=0
    for i in range(start,5):
        count+=cs(n-1,i)
    return count
def cvs(n):
    return cs(n,0)
n=int(input("ENTER THE VALUE OF N---> "))
if(n<0):
    print("NEGATIVE VALUE")
else:
    print(cvs(n))
