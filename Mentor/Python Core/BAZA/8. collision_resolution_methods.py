'''

LOAD_FACTOR = SIZE / CAPACITY 
When 0.7 is reached, the hash table should be resized.


1) На основе цепочек
    Внутри слота хэщ-таблицы находится связанный список ключей и соответствующих им значений. 
    + прост в реализации
    + требует небольшой памяти
    - может увеличить время поиска в случае большого числа коллизий
2) Открытая адресация
    Если занято - иди в следующий
    + не использует памяти
    - увеличиваетк оличество коллизий 

3) Rehashing.
    Этот метод состоит в увеличении размера таблицы при достижении определенного
    порога заполнения. При этом все элементы таблицы перемещаются в новые слоты 
    с новыми хэш-значениями. Rehashing обычно используется совместно с другими
    методами разрешения коллизий.
'''