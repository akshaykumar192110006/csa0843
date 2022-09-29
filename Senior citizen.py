p=int(input("Enter2000 the Principal Amount:"))
t=int(input("Enter Number of Years="))
s=input("Is the Customer Senior Citizen:")
y='yes'
n='no'
if(s==y):
    simple_interst=(p*t*12)/100
    print("simple interst=",simple_interst)
elif(s==n):
    simple_interst=(p*t*10)/100
    print("simple interst=",simple_interst)
else:
    print("INVALID INPUT")

