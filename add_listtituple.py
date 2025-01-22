#Adding list to tuple
def concate(lst, tup):
    x = tuple(list(lst) + list(tup))  
    return str(x)

lst = [1, 2, 3]
tup = (4, 5, 6)
print(concate(lst, tup))
