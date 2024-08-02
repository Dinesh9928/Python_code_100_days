tup = (1, 2, 76, 342, 32, "green", True)
tup[0] = 90 # typeError 
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[34]) #indexError

if  342 in tup:
  print("Yes 342 is present in this tuple")
else:
  print("no not there")
  
tup2 = tup[1:4]
print(tup2)
