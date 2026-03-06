"""
It is represented as[]
It is mutable
Built-in-methods:
append()
insert()
extend()
pop()
remove()
clear()
sort(),sort(reverse = True)
reverse()
index() return index
count()
copy()
max()
min()
len()
list()
sorted()
reversed()
"""
"""
# Leat code questions
#1480
li = list(map(int,input().split()))
li1 = []
total = 0
for i in li:
    total += i
    li1.append(total)
print(li1)

"""
"""
Nums = [1,2,3,1]
S = set(Nums)
if S == Nums:
    print(False)
else:
    print(True)

"""
#1672. Richest Customer Wealth 
acc = [[1,2,3],
       [3,2,1]]
max_sum = sum(acc[0])
for i in range(len(acc)):
    if sum(acc[i]) > max_sum:
        max_sum = sum(acc[i])
print(max_sum)