# def my_range(start, stop, step=1):
#   numbers = []
#   i = start
#   while i < stop:
#     numbers.append(i)
#     i += step
#   return numbers


# print(my_range(1, 10)) 
# print(my_range(1, 10, 2))  
# print(my_range(5, 1, -1))  


def my_range(start=0, stop=None, step=1):
    numbers = []
    if step == 0:
        raise ValueError("Step cannot be zero")
    if step > 0: # noldan katta bo'lganida qiymat qoshib ketish
        i = start # start qiymatidan foydalanish uchun o'zgaruvchi ovolish
        while i < stop: # i(start) Stop  dan teng bo'lgunga qadar True bo'ladi
            numbers.append(i)  # numbers listga i(start) ni qoshib ketadi
            i += step # i ni qiymatini stepga bitta qoshib boriyabdi
    else:
        i = start # start qiymatidan foydalanish uchun o'zgaruvchi ovolish
        while i > stop: # stop i ga teng bo'lguncha boladi. 
            numbers.append(i) # # numbers listga i(start) ni qoshib ketadi
            i += step # i ni qiymatini stepga bitta qoshib boriyabdi
    return numbers
print(my_range(1, 10))
print(my_range(1, 10, 2))
print(my_range(5, 1, -1))
