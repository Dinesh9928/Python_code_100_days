tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)

ind1 = tuple1.index(3)
print(ind1)

ind2 = tuple1.index(3, 4, 8) # start = 4 end = 8 index range
print(ind2)

res = tuple1.index(311) # valueError 
res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)
print(res)
