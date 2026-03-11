'''
#1. write python code to print all the arithmetic operators(+,-,*,/,//,**,%)?
print(abs(-54))
print(round(5,478))
print(min([10,20,30,40,54,2]))
print(max([10,20,30,40,54,2]))
print(sum([10,20,30,40,54,2]))
print(pow(2,5))

import math
print(math.sqrt(81))
print(math.ceil(4,2))


'''
#1. find the gcd (using math module and using euclidean method)

a=int(input())
b=int(input())
while b != 0:
    a,b=b, a%b 
print(a)

import math
a=int(input())
b=int(input())
print(math.gcd(a,b))

#2. Find the LCM 
import math
a=int(input())
b=int(input())
gcd=math.gcd(a,b)
lcm=(a*b)//gcd
print(lcm)
