''' Задача 24:  '''

from random import randint

kust_count = int(input('Укажите количество кустов '))
max_berry_count = int(input('Укажите максимально возможное количество ягод '))
berry_count = [randint(0, max_berry_count) for x in range(kust_count)]
sum_harvest = []
order_of_bushes = []

for j in range(kust_count):

    harvest = []
    for i in range(1, kust_count-1, 3):
        val = berry_count[i-1] + berry_count[i] + berry_count[i+1]
        harvest.append(val)

    order_of_bushes.append(berry_count)
    sum_harvest.append(sum(harvest))
    temp_val = berry_count[0]
    berry_count.pop(0)
    berry_count.append(temp_val)
    
max_harvest = max(sum_harvest)
ind_max_harvest = sum_harvest.index(max_harvest)
print('')
print(f'Наибольшая урожайность с одной итерации {max_harvest}')
print(f'При следующем расположении кустов и ягод на них: {order_of_bushes[ind_max_harvest]}')