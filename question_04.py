question_04 ="""
Rotating primes

Given an integer n, return whether every rotation of n is prime.
Example 1:
Input:
n = 199
Output:
True
Explanation:
199 is prime, 919 is prime, and 991 is prime.

Example 2:
Input:
n = 19
Output:
False
Explanation:
Although 19 is prime, 91 is not.

Write your code bellow
"""
n=int(input("PLease enter the number to rotate and check"))
n=str(n)
l=[]
for i in range(len(n)):
    l.append(n[i:] + n[:i])
print(l)
c=0
for j in range(len(l)):
    x=int(l[j])
    for k in range(2,x):
        if x%k==0:
            #print("False")
            break
    c+=1
if c==len(l):
    print("True")
else:
    print("False")