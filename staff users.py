tu=int(input("ENTER THE TOTAL USERS----> "))
if(tu<=0):
    print("VALUE ERROR")
su=int(input("ENTER THE STAFF USERS----> "))
if(su<=0):
    print("INVALID")
a=su/3
stu=tu-su-a
print("STUDENT USERS--- > ",stu)

