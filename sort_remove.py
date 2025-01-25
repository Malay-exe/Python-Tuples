#remove the kth element from the given tuple after sorting
def rem(t,k):
    x=sorted(t)
    return tuple(x[:k]+x[-k:])
tup=(1,2,3,4,5)
k=2
print(rem(tup,k))