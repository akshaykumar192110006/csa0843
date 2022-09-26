def wc(d,a):
    area=0
    for i in range(a):
        for j in range(i+1,a):
            area=max(area,min(d[j],d[i])*(j-1))
    return area
arr=[]
n=int(input("ENTER THE NUMBER OF ELEMENT---> "))
for i in range(0,n):
    ele=int(input("ENTER THE ELEMENTS---> "))
    arr.append(ele)
s=len(arr)
print(wc(arr,s))
