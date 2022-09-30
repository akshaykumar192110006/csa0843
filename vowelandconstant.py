s=input("ENTER THE STRING----> ")
vowel=0
constant=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowel=vowel+1
    else:
        constant=constant+1
print("NUMBER OF VOWELS---> ",vowel)
print("NUMBER OF CONSTANTS---> ",constant)

