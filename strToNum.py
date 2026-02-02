def strToNum(s):
    num=0
    Sum=0
    #Convert character to digit
    for ch in s:
        digit=ord(ch)-ord('0')
        num=num*10+digit
    # sum of digits
    while num!=0:
        rem=num%10
        Sum+=rem
        num=num//10
    print(Sum)
s=input()
strToNum(s)