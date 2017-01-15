# -*- coding: utf-8 -*-

import math
import random
import simpy

customers_count = 0
total_latency = 0
log_fd = open('single.log', 'a')


def cur_time(environment):  # получение времени в читаемом виде для логов
    seconds = environment.now
    hours = int(seconds / 3600) % 24 + 9  # магазин начинает работу с 9 часов утра
    minutes = int(seconds % 3600 / 60)
    return '{0:02}:{1:02}:{2:02}'.format(hours, minutes, int(seconds % 60))


def customer_behaviour(name, environment, boxes):
    purchases_count = random.gammavariate(12, 1)
    print >> log_fd, cur_time(environment), 'Зашел покупатель #', name
    yield environment.timeout(purchases_count * random.normalvariate(3, 0.2) * 60)  # в минутах
    print >> log_fd, cur_time(environment), len(boxes.queue), 'покупателей находятся в очереди'
    global total_latency
    with boxes.request() as box:
        print >> log_fd, cur_time(environment), 'Покупатель #', name, 'встал в очередь'
        start = environment.now
        yield box
        print >> log_fd, cur_time(environment), 'Покупатель #', name, 'обслуживается'
        yield environment.timeout(random.normalvariate(5, 0.2) * purchases_count)  # в секундах
        total_latency += environment.now - start
    print >> log_fd, cur_time(environment), 'Покупатель #', name, 'обслужен'


def incoming_customer(environment, boxes):
    global customers_count
    while environment.now < work_hours:  # если магазин работает, приходит новый покупатель
        customers_count += 1
        environment.process(customer_behaviour(customers_count, environment, boxes))
        yield environment.timeout(random.expovariate(0.3))
    print >> log_fd, cur_time(environment), 'Магазин закрыт'

print >> log_fd, 'Магазин открыт'

print 'Укажите время работы магазина в часах:',
work_hours = input() * 3600
print 'Укажите число касс:',
k = input()

env = simpy.Environment()
cash_boxes = simpy.Resource(env, k)
env.process(incoming_customer(env, cash_boxes))
env.run()

print 'Время ожидания составило', int(math.ceil(total_latency / customers_count)), 'секунд в среднем'
