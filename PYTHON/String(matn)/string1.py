# O'zgaruvchiga satr tayinlash

name = "islomjon"
print(name) 

# Ko'p qatorli matn yaratish

Lorem = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(Lorem) 


# Satrlar massivlardir

name = "islomjon"
print(name[3]) 


# Matnni raqamlar index aylantirish

for x in "banana":
  print(x)
  
  
# String uzunligi

a = "Hello, World!"
print(len(a))

# Matnni ichidagi so'zni tekshirish
txt = "The best things in life are free!"
print("free" in txt)
# if bilan bajarish
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
# NOT ligini tekshiring

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")