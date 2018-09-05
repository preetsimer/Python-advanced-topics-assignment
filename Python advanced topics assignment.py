#Question 1

l=[]
n=int(input("Enter size: "))
print("Enter numbers: ")
for i in range(0,n):
    a=int(input())
    l.append(a)
l=[i**3 for i in l]
print(l)


#Question 2
l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))
a=[i for i in range(l,u)  for j in range(2,i) if(i%j==0)  ]
b=[i for i in range(l,u) if(i not in a )]
print(b)


#Question 3

'''
In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The type of data returned by list comprehensions and generator expressions differs.
The generator yields one item at a time — thus it is more memory efficient than a list.'''

#Lambda and Map

#Question 1

Celsius=[39.2 ,36.5, 37.3, 37.8]
fahrenhiet=list(map(lambda x: 1.8*x+32,Celsius))
print(fahrenhiet)

#Question 2

l=[]
n=int(input("Enter Size: "))
print("Enter nummbers: ")
for i in range(0,n):
    a=int(input())
    l.append(a)
def squ(n):
    return n*n
l2=list(map(lambda n:squ(n),l))
print(l2)

#Filter and Reduce


#Question 1

l=[]
n=int(input("Enter Size: "))
print("Enter nummbers: ")
for i in range(0,n):
    a=int(input())
    l.append(a)
def isprime(n):
    flag=1
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                flag=0
                break
        if(flag==1):
            return n
l2=list(filter(lambda n: isprime(n),l))
print(l2)


#Question 2
l=[]
n=int(input("Enter Size: "))
print("Enter nummbers: ")
for i in range(0,n):
    a=int(input())
    l.append(a)
from  functools import *
m=reduce(lambda x,y:x*y,l)
print(m)
