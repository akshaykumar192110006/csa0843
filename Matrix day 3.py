A=[]
n=int(input("ENTER THE MATRIX A---> "))
print("ENTER THE ELEMENT---> ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    A.append(row)
print(A)
print("MATRIX A")
for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")
    print()
B=[]
n=int(input("ENTER THE MATRIX B---> "))
print("ENTER THE ELEMENT---> ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    B.append(row)
print(B)
print("MATRIX B")
for i in range(n):
    for j in range(n):
        print(B[i][j],end=" ")
    print()
C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(n):
    for j in range(n):
        C[i][j]=A[i][j]+B[i][j]
for d in C:
    print("MATRIX C",C)
