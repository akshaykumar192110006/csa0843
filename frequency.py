n=int(input("ENTER NUMBER OF ELEMENTS---> "))
arr=[]
for i in range(0,n):
    a=input("ENTER THE ELEMENTS---> ")
    arr.append(a)
print(arr)
#Array fr for storing count of elements  
fr = [None] * len(arr);    
visited = -1;    
     
for i in range(0, len(arr)):    
    count = 1;    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            count = count + 1;    
            #To avoid counting same element again    
            fr[j] = visited;    
                
    if(fr[i] != visited):    
        fr[i] = count;    
     
#Displays the count of times array element is present    
print("---------------------");    
print(" Element | Count");    
print("---------------------");    
for i in range(0, len(fr)):    
    if(fr[i] != visited):    
        print("    " + str(arr[i]) + "    |    " + str(fr[i]));    
print("---------------------");
