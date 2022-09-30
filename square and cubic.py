try:
    n=float(input("ENTER THE DECIMAL VALUE---> "))
    sq=n*n
    cu=n*n*n
    print("SQUARE OF THE VALUE---> ",sq)
    print("CUBE OF THE VALUE---> ",cu)
except(ValueError):
    print("VALUE ERROR")
