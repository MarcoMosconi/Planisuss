import string
import random

# initializing size of string
N = 7

# using random.choices()
# generating random strings

def generateKey():

    res = ''.join(random.choices(string.ascii_uppercase +
							string.digits, k=N))
    return res