# s= {1,2,3,4,5,66,5,3, 'himanshu','himanshu'}
# print(s,type(s))
# s.add(9)
# print(s)

s1 = {1,3,4,6,32}
s2 = {77,4,3,8,9}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
print({3,4}.issubset(s1))
