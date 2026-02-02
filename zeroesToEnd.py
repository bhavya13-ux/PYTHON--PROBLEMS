def moveZeroToEnd(a):
    n=len(a)
    j=0
    #encounter first zero from the array
    while j<n and a[j]!=0:
        j+=1
    i=j+1
    while j<i and i<n:
        if a[i]!=0:
            a[j],a[i]=a[i],a[j]
            j+=1
        i+=1
    print(a)      
a=list(map(int,input().split()))
moveZeroToEnd(a)