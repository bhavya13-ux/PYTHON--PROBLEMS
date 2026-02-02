#Deloitte NLA
# Problem Statement : You are given an array of integers. Your task is to find the two numbers that appear most frquently in the array. If two numbers have the same frequency, choose the larger one. Then calculate the average of all occurences of these two numbers and return the floor of the result.
def twoModes(arr):
    d={}
    for num in arr:
        d[num]=d.get(num,0)+1

    maxKey=maxValue=0
    secMaxKey=secMaxValue=0

    for key in d:
        if d[key]>maxValue or(d[key]==maxValue and key>maxKey):
            maxValue=d[key]
            maxKey=key

    for key in d:
        if d[key] < maxValue and (
            d[key] > secMaxValue or
            (d[key] == secMaxValue and key > secMaxKey)
        ):
            secMaxValue=d[key]
            secMaxKey=key

    result=((maxKey*maxValue)+(secMaxKey*secMaxValue))//(maxValue+secMaxValue)
    return result

arr=list(map(int,input().split()))
print(twoModes(arr))
