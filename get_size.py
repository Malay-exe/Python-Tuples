#how to get the size of the tuple
import sys as s
def size(tup):
    print("Size of the Tuple is :",s.getsizeof(tup),"Bytes")
tup=("A", 1, "B", 2, "C", 3)    
size(tup)