'''
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

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)


n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(j) for j in range(1,i+1)]))

for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(i) for j in range(1,i+1)]))
'''

n = int(input())
val = 65
for i in range(n):
    for j in range(i+1):
        print(chr(val),end=" ")
        val += 1    
    print()