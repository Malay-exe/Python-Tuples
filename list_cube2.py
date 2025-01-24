#Create a list of tuples from given list having number and its cube in each tuple
def cube(t):
    x = []
    for i in t:
        x.append((i, i**3))
    return x 
print(cube([1,2,3,4,5]))