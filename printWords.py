#print each word of a string in separate lines
def printWords(s):
    i=0
    n=len(s)
    while i<n:
        word=''
        while i<n and s[i]!=" ":
            word+=s[i]
            i+=1
        if word!='':
            print(word)
        i+=1
s=input()
printWords(s)