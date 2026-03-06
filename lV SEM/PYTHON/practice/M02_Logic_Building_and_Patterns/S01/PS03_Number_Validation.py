'''
#1. write a problem code for the factorial

n=int(input(" enter n "))
fact = 1
for i in range(1, n+1):
    fact * i
print(fact)

# 2. write a python code to check whethera number is amstrong or not
# ex: 153-->1,5,3-->(1*3)+(5*3)+(3*3)=153

n=int(input(" enter n "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if n==sum:
    print(n," is amstrong")
else:
    print(n," is not amstrong")

# 3. write a python code to check whether a number is prime or not
n=int(input(" enter n "))
is_prime=True
if n<2:
    is_prime=False
else:
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
if is_prime:
    print(n," is prime")
else:
    print(n," is not prime")

# 4. print the prime numbers with range?

# Monotic of an array?

arr=list(map(int,input("Enter array ele: ").split()))
inc=True
dec=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        inc=False
    if arr[i]<arr[i+1]:
        dec=False
if inc or dec:
    print("monotonic")
else:
    print("not monotonic")

#reverse integer:
#given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
#assume the environment does not allow you to store 64-bit integers (signed or unsigned).

x=int(input("Enter an integer: "))
sign=1
if x < 0:
    sign = -1
    x = -x
rev=0
while x > 0:
    digit = x % 10
    rev = rev * 10 + digit
    x //= 10
rev *= sign
if rev < -2**31 or rev > 2**31 - 1:
    print(0)
else:
    print(rev)


#give a roman numerical, convert it to an integer.
roman = input("Enter a roman numeral: ").upper()
values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
total = 0
prev_value = 0
for ch in reversed(roman):
    if values[ch] < prev_value:
        total -= values[ch]
    else:
        total += values[ch]
    prev_value = values[ch]
print("Integer value:", total)
# Return true if n is a happy number, and false if not.
li = [1,2,3,4,5]
#output : [2,4,6,8,10]
res = []
for ele in li:
    res.append(ele * 2)
print(res)

print([ele * 2 for ele in li]) 
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

print([i for i in li if i % 2 == 0])
print(tuple(i for i in li if i % 2 == 0))
print({i:i*2 for i in li if i % 2 == 0})

li1 = ['a','b','c']
#"a b c"
res= ""
for ch in li1:
    res = res + ch + " " 
print(res)

print(" ".join(li1))

#1.Pyramid
n=4
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

#reverse pyramid
n=4
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

'''

