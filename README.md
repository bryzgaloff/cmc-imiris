## Отчет по второму практическому заданию курса "Имитационное моделирование в исследовании и разработке информационных систем"

### Постановка задачи
Моделирование работы магазина самообслуживания (вариант 4).

Покупатель входит в магазин (интервал времени между входящими — случайная величина с рапределением D<sub>enter</sub>), набирает в тележку n<sub>i</sub> единиц товара (распределение D<sub>num</sub>), тратя на это время t<sub>i</sub> (распределение D<sub>time</sub>, среднее зависит от n<sub>i</sub>), и встаёт в очередь к одной из касс. Общее число касс k. Время обслуживания покупателя в кассе задаётся случайной величиной с распределением D<sub>pay</sub>, среднее значение зависит от числа покупок. Правила выбора кассы могут быть различными (см. ниже).

Требуется построить модель, отражающую состояние очередей к кассам и общее число покупателей в торговом зале. Задать распределения D<sub>enter</sub>, D<sub>num</sub>, D<sub>time</sub>, D<sub>pay</sub> на основе интуитивных предположений и / или наблюдений, задать параметры распределений (по согласованию с преподавателем).

Провести серию экспериментов с моделью и определить зависимость среднего времени ожидания покупателя в очереди к кассе от числа касс и правил выбора кассы. Ещё вариант: время ожидания, делённое на число покупок.

Возможные правила выбора кассы (список может быть дополнен по усмотрению студента,  исполнителю задания не требуется выбирать  все пункты, объём исследования берётся по  согласованию с преподавателем):
* покупатель случайно выбирает кассу (задать распределение);
* покупатель идёт к кассе с очередью наименьшей длины (в людях);
* есть кассы для числа покупок «не более чем», покупатели строго следуют указанному ограничению; (предусмотреть исследование числа таких касс)

Дополнительно: провести исследование, каково должно быть  минимальное число касс для того, чтобы время ожидания было в пределах допустимого (оптимизация в пользу магазина).

### Распределения
Зададим следующие распраделения, необходимые для решения задачи:
* Интервал между входящими покупателями — случайная величина, заданная экспоненциальным распределением D<sub>enter</sub> (известно из курса теории вероятностей) с параметром 0.20.
* Количество покупок — случайная величина, заданная гамма-распределением D<sub>num</sub> с параметрами (15.00, 1.00).
* Время покупки и время обслуживания покупателя — заданы нормальным распределением (D<sub>time</sub> и D<sub>pay</sub>) с параметрами (2.00, 0.20) и (5.00, 0.20) соответственно. Такой выбор сделан в силу того, что все в среднем тратят одинаковое время.

### Замечания по реализации
Для реализации использован Python 3.5 и [SimPy](https://simpy.readthedocs.io/) — фреймворк процессо-ориентированной дискретно-событийной системы моделирования<sup>[wiki](https://ru.wikipedia.org/wiki/SimPy)</sup>.
