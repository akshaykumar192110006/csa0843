def addbin(a,b):
    ml=max(len(a),len(b))
    a=a.zfill(ml)
    b=b.zfill(ml)
    res=''
    carry=0
    for i in range(ml-1,-1,-1):
        r=carry
        r+=1 if a[i]=='1' else 0
        r+=1 if b[i]=='1' else 0
        res=('1' if r%2==1 else '0')+res
        carry=0 if r<2 else 1
    if carry!=0: res='1'+res
    return res.zfill(ml)
a=input("ENTER THE VALUE OF A BINARY NUMBER---> ")
b=input("ENTER THE VALUE OF B BINARY NUMBER---> ")
print(addbin(a,b))
