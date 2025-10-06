
n = int(input("entrer le nombre  ")) 
k=n//3
for i in range(k):
    for j in range(n,n-3,-1):
        print(j , end="")
    n= n-3   
    print(" ") 
