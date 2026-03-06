'''
#Adding Elements
A = {1,2,3}
B = {3,4,5}
A.add(4)
B.update({6,7})
print(A,B)

#Remove Elements
A.pop()
print(A)
A.remove()

'''

#Missing number
nums = [3,0,1]
n = len(nums)
res = set(range(n+1))
li = nums
print(int(res - set(li)))
