# Given two numbers M and N, write a program to find the sum S of the prime numbers between (and including) the two numbers, and print the factors of S as output.

# Factors are numbers which divide the given number without any remainder.
# For example, the factors of 24 are 1, 2, 3, 4, 6, 8, 12, and 24.
# Note: 1 is not considered a prime number.

# Read the input from STDIN and print the output to STDOUT.
# For some languages, the reading input & printing output code may already be provided in the coding window. Please check.
# Do not print arbitrary strings in the code, as these contribute to the output and test cases will fail.
from math import sqrt
a=int(input())
b=int(input())
Sum=0
lst=[]

for num in range(a,b+1):
    if num<2:
        continue
    flag=False
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            flag=True
            break
    if not flag:
        Sum+=num
for factor in range(1,Sum+1):
    if Sum%factor==0:
        lst.append(factor)
print(lst) 