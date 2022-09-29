string=str(input("ENTER THE STRING---> "))
string=string.casefold()
revstring=reversed(string)
if list(string)==list(revstring):
    print("THE STRING ENTERED IS A PALINDROME")
else:
    print("THE STRING IS NOT A PALINDROM")
