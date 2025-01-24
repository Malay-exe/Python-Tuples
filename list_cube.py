#Create a list of tuples from given list having number and its cube in each tuple
def cube(t):
    x = [(i, i**3) for i in t]
    return x 
print(cube([1,2,3,4,5]))   