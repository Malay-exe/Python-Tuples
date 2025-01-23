#Adding Tuple to List 
def concate(lst,tup):
    lst+=tup 
    return lst
lst=[1,2,3]
tup=(4,5,6)
print(concate(lst,tup))