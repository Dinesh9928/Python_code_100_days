l = [11, 45, 1, 2, 4, 6, 1, 1]

l.append(7)
print(l)
l.sort(reverse=True)
l.sort()
l.reverse()
print(l.index(1))
print(l.index(3)) # gives valueError when ele present
print(l.count(1))

m = l.copy()
m[0] = 0  # 0 index ele removed
l.insert(0, 0) # the ele not removed, insert at index by adjusting exsisting value. 
# print(l)
# print(m)
l.insert(1, 899)

m = [900, 1000, 1100]
# k = m + l
# print(k)
l.extend(m) # l = l + m 
print(l)
