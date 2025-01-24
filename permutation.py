#print all pair combinations of 2 tuples
def combination(t1,t2):
    x=[]
    for i in t1:
        for j in t2:
            x.append((t1,t2))
            # x.append((t2,t1))         
    return x
t1=(4,5)
t2=(7,8)
print(combination(t1,t2))