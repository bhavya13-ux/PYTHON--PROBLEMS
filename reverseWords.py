#print reverse words
def reverseWords(s):
    i=0
    n=len(s)
    reverse=''
    while i<n:
        word=''
        while i<n and s[i]!=" ":
            word+=s[i]
            i+=1
        if word!='':
            reverse=word+" "+reverse
        i+=1
    print(reverse)
s=input()
reverseWords(s)