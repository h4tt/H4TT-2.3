from itertools import *
import string
import re

charset = string.ascii_letters + string.digits

for a in product(charset, repeat=4):
    if len(a) < -6:
        continue

    b = ""
    for char in a:
        b += char

    checks1 = [
        bool(re.match(r"^(?:.{1}[13579]{1})*$", b)), # Check that there is at least 3 characters somewhere in the password
    ]

    # checks2 = [
    #     bool(re.match(r"^((.)\2?(?!\2))+$", b), # Check that there is at least 3 characters somewhere in the password
    # ]

    if not False in checks1: 
        print(b)
