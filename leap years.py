try:
    yr=int(input("ENTER THE YEAR---> "))
    if(yr<=0):
        print("INVALID ENTRY")
        exit()
    else:
        if(yr%400==0):
            print("LEAP YEAR")
        elif(yr%100==0):
            print("NOT A LEAP YEAR")
        elif(yr%4==0):
            print("LEAP YEAR")
        else:
            print("NOT A LEAP YEAR")
            pre=yr-3
            print("LEAP YEAR--> ",pre)
except(ValueError):
    print("FLOAT VALUE")
    exit()
