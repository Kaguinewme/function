
list=[1,2,3,3,3,3,4,5,6,6,7,8,8]
def unique(list):
  i=0
  b=[]
  while i<len(list):
    if list[i] not in b:
      b.append(list[i])
    i+=1
  return b
print(unique(list))