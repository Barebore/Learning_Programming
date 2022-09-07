'''
У вас есть 1000$, которую вы планируете эффективно вложить. Вам даны цены за 1000 кубометров газа за n дней. Можно один раз купить газ на все деньги в день i и продать его в один из последующих дней j, i < j.

Определите номера дней для покупки и продажи газа для получения максимальной прибыли.

Формат ввода
В первой строке вводится число дней n (1 ≤ n ≤ 100000).

Во второй строке вводится n чисел — цены за 1000 кубометров газа в каждый из дней. Цена — целое число от 1 до 5000. Дни нумеруются с единицы.

Формат вывода
Выведите два числа i и j — номера дней для покупки и продажи газа. Если прибыль получить невозможно, выведите два нуля.'''

n= int(input())
cost = list(map(int, input().split()))
bestBuyDay = 0
bestSellDay = 0
minCostDay = 0
for i in range(1,n):
    if cost[bestSellDay] * cost[minCostDay] < cost[bestBuyDay] * cost[i]:
        bestBuyDay = minCostDay
        bestSellDay = i
    if cost[i] < cost[minCostDay]:
        minCostDay = i
if bestSellDay == 0 and bestBuyDay == 0:
    print(0,0)
else:
    print(bestBuyDay + 1, bestSellDay + 1)