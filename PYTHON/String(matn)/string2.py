""" 
Python - Stringlarni kesish
"""

# b = "Hello, World!"
# print(b[2:5])
# #llo

# b = "Hello, World!"
# print(b[:5])
# #Hello

# b = "Hello, World!"
# print(b[2:])
# #!llo, World

# b = "Hello, World!"
# print(b[-5:-2])
# #orl


"""" 
Python - satrlarni o'zgartirish
"""


# upper() usuli satrni katta harf bilan qaytaradi:
a = "Hello, World!"
print(a.upper())

# upper() usuli satrni katta harf bilan qaytaradi:
a = "Hello, World!"
print(a.lower())

# Bo'sh joyni olib tashlang

a = " Hello, World! "
print(a.strip()) # returns "Hello,      World!


# Stringni almashtiring / replace() usuli satrni boshqa satr bilan almashtiradi:
a = "Hello, World!"
print(a.replace("H", "J"))

# Split() usuli ko'rsatilgan ajratuvchi orasidagi matn ro'yxat elementlariga aylanadigan ro'yxatni qaytaradi.

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 