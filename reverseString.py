#Deloitte NLA question
#1.Given a string Str and a positive integer M, write a program to print Str with the first M characters reversed.
# For example, if M = 3, then the first three characters from Str need to be reversed and the rest of the characters printed as it is.
# If M is less than the length of Str, then keep reversing until M reversals are done.

# Read the input from STDIN and print the output to STDOUT.
# Do not write arbitrary strings while reading the input or while printing to the standard output.

# Constraints
# Length of Str > 1
# Str can contain upper-case or lower-case letters, but no spaces, numbers, or special characters

# Input Format
# The first line of input contains a string Str.
# The second line of input contains M.
def doAction(lst,k):
    i=0
    j=k-1
    while i<=j:
        lst[i],lst[j]=lst[j],lst[i]
        i+=1
        j-=1
    result=''.join(lst)
    return result

def reverseString(s,k):
    lst=list(s)
    n=len(lst)
    if k<=n:
        print(doAction(lst,k))
    elif k>n:
        lst[::]=lst[::-1]
        rem=k-n
        print(doAction(lst,rem))
s=input()
k=int(input())
reverseString(s,k)