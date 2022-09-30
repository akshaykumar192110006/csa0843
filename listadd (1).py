l1=[]
l2=[]
c1=[]
c2=[]
n=int(input("ENTER NUMBER OF ELEMENTS in L1---> "))
for i in range(0,n):
    a=int(input())
    l1.append(a)
    c1.append(l1[i])
print(c1)
m=int(input("ENTER NUMBER OF ELEMENTS in L2---> "))
for i in range(0,m):
    b=int(input())
    l2.append(b)
    c2.append(l2[i])
print(c2)
c3=c1+c2
c3.sort()
print(c3)
