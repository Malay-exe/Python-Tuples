#remove the tuple of kth length
def rem(lst,k):
    x=[]
    for i in lst:
        if len(i)!=k:
            x.append(i)
    return x
tup=[(1,2),(4,5,6),(2,4),(6,4,5,7),(1,)]
k=1
print(rem(tup,k))