def binary_search(list,item):
    low = 0
    high = len(list)-1
    i = 1
    #print('low =',low,'high =', high)
    while low <= high:
        mid = (low+high)//2
        print('Пошёл цикл №', i,'mid =' ,mid)
        guess = list[mid]
        #print('guess = ',guess,'item =',item)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
            #print('hight (mid-1) = ',high)
        else:
            low = mid + 1
            #print('low(mid+1) = ',low)
        i = i + 1
    return None

import time
start_time = time.time()
# тут играюсь со скоростью заполнения массива, через лист в 10 раз быстрее
#my_list = []
#for i in range(100000000):
#    my_list.append(i)
my_list = list(range(0,4000000000))
#print(my_list[174])
#тут играюсь с поиском индекса значения в массиве, тоже получается слишком долго
# с бинарным поиском сильно быстрее
#for i in range(len(my_list)):
#    if my_list[i] == 90000000:
#        print('exelent')
print('OTVET',binary_search(my_list, 3))
#print('OTVET',binary_search(my_list, 10000000))
#print('OTVET',binary_search(my_list, 10000000))
#print('OTVET',binary_search(my_list, 10000000))
#print('OTVET',binary_search(my_list, 10000000))
#print('OTVET',binary_search(my_list,-1))

print("--- %s seconds ---" % (time.time() - start_time))


print('THIS IS POWER OF GIT')

print('THIS IS POWER OF GIT')