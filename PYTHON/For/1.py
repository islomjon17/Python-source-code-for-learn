def raqam_bor(name):
    for char in name:
        if char.isdigit():
            return True
    return False

# Test the function
name1 =  input()
name2 =  input()
print(raqam_bor(name2))
print(raqam_bor(name1))
"""
code for check string iclude number or not. If input int or include integers return this is cann not be name, except this is can be name

"""


