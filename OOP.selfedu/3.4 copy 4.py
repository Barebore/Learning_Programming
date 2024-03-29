class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        return self.money + other
    
    def __radd__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        return self.money + other
    


class Budget:
    def __init__(self):
        self.budg = []

    def add_item(self, it):
        self.budg.append(it)

    def remove_item(self, indx):
        del(self.budg[indx])

    def get_items(self):
        return self.budg
    
my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
