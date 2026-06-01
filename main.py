#15-m
class Home:
    def __init__(self, adrees, price):
        self.adrees = adrees
        self.__price = price
        
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        self.__price = new_price
        
h1 = Home("Mystic falls", "1,000,000,000$")

print(h1.adrees)
print(h1.get_price())

h1.set_price("1,000,000,000,001$")
print(h1.get_price())
