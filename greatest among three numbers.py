#program to find greatest of three numbers
a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))
if(a>b and a>c):
      print("a is greatest:",a)
elif(b>c and b>a):
      print("b is greatest:",b)
else:
      print("c is greatest:",c)
      
