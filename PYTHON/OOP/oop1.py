## DUNDER METODLARI

class Cars:
    __num_car = 0
    """ Classes of cars """
    
    def __init__(self, make, model, color, year, price):
        self.make = make
        self.model = model
        self.color = color 
        self.year = year
        self.price =price
        
        Cars.__num_car += 1
        
    def __str__(self):
        return f"Car: {self.make} {self.model}"
        
    def __eq__(self, y):
        return self.price==y.price
    
    def __lt__(self,y):
        return self.price==u.price
        
# car1 = Cars("BYD", "Song plus", "Black", 2023, 50000)
# print(car1)


car1 = Cars("BYD", "Song plus", "Black", 2023, 50000)
car12 = Cars("BYD", "Chazor", "Black", 2023, 56000)
# car13 = Cars("BYD", "Hang", "Black", 2023, 60000)
# car14  = Cars("TESLA", "X", "Black", 2023, 80000)
# car15 = Cars("TESLA", "y", "Black", 2023, 89000)
# car16 = Cars("TESLA", "S", "Black", 2023, 90000)