"""Returns x * 2"""
def db(x):
    return x * 2

"""Returns (x+1)^(x+1)""" # Line 1-2 changed in u1

def ex(x):
    print("Input is", x)
    x = x + 1 # Adds 1 to x
    return x**x
# This line changed in u0 # and again in u1
print(ex(1))
print(db(10))