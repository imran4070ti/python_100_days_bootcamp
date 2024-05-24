# In python we often declare constant as global variable with capital letter

PI = 3.14158 # Like this
pi = 3.14159 # Not like this

def area_of_triangle(r):
    return PI*r**2


print(area_of_triangle(4))