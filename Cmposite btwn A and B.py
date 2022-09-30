m=int(input('Enter A: '))
n=int(input('Enter B: '))
for number in range(m+1,n):
    factor=0
    for i in range(1,number):
      if number%i==0:
        factor=i
    if factor>1:
      print (number)
