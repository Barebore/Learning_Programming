lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']

class ListObject:
    def __init__(self, data, next_obj = None):
        self.next_obj = next_obj
        self.data = data
    
    def link(self, obj):
        self.next_obj = obj

lst = []
for i in lst_in:
    lst.append(ListObject(i))

for i in range(len(lst)-1):
    lst[i].link(lst[i+1])

head_obj = lst[0]