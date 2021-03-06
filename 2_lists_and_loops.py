########################################################################################################################

# 4 - Строки

# Solution:

heart = '❤️'
fire = '🔥'
shrug = '🤷'

print(heart)
print(fire)
print(shrug)

########################################################################################################################

# 5 - Списки

"""
Задание
Посчитаем долю выбранных эмодзи среди всех. Для этого сначала найдите сумму первых пяти элементов подготовленного
списка emojixpress. Но складывайте не сами числа, а элементы, полученные по индексу. Напечатайте результат на
экране (формат вывода уже задан в прекоде)
"""

# Solution:

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]

total = emojixpress[0] + emojixpress[1] + emojixpress[2] + emojixpress[3] + emojixpress[4]
print("{:.2f}".format(total))

########################################################################################################################

# 6 - Циклы

"""
Задание
Всего в сообщениях с клавиатурой EmojiXpress отправлено 1.72 миллиарда, или 1720 миллионов, эмодзи (источник
EmojiStats, данные на конец 2018). Для каждого эмодзи из первых десяти посчитайте их долю среди всех. Затем выведите
её в процентах с точностью до одного знака после запятой, в следующем формате:

Доли эмодзи:
0.1%
1.1%
...

Всего эмодзи: 1.72 млрд

Обратите внимание, что перед последней строкой нужно поставить дополнительный перенос строки для большей наглядности
"""

# Solution:

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]

# количество всех эмодзи в миллионах
emojixpress_total = 1720

# < напишите код здесь >
print('Доли эмодзи:')
for item in emojixpress:
    part = item / emojixpress_total
    print('{:.1%}'.format(part))

print()
print('Всего эмодзи: 1.72 млрд')

########################################################################################################################

# 7 - Оператор присваивания со сложением

"""
Задание
Давайте посчитаем суммарное количество рук на нескольких случайных эмодзи: 😘, 👍, 🤣, 😉, 🤔 и 🤷. Допишите
программу для решения этой задачи
"""

# Solution:

total_hands = 0

# эмодзи "Поцелуй"
total_hands += 0

# эмодзи "Класс"
total_hands += 1

# эмодзи "Катаюсь от смеха"
total_hands += 0

# эмодзи "Подмигиваю"
total_hands += 0

# эмодзи "Задумчивость"
total_hands += 1

# эмодзи "Пожимаю плечами"
total_hands += 2

print(total_hands)

########################################################################################################################

# 7.2 - Оператор присваивания со сложением

"""
Задание
Оператором присваивания со сложением посчитайте суммарное количество первых пяти эмодзи. Промежуточные значения
и конечный результат сохраняйте в переменной total. В конце напечайте на экране её значение с точностью до двух знаков
после запятой (уже сделано в прекоде)
"""

# Solution:

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2]

# приравняйте переменную total к нулю
total = 0

# прибавьте значение с индексом 0
total += 2.26

# прибавьте значение с индексом 1
total += 19.1

# прибавьте значение с индексом 2
total += 25.6

# прибавьте значение с индексом 3
total += 233.0

# прибавьте значение с индексом 4
total += 15.2

print('{:.2f}'.format(total))

########################################################################################################################

# 8.1 - Циклы с изменением значений переменных

"""
Задание
Теперь мы можем оценить, какую долю в EmojiXpress составляют выбранные нами эмодзи. Всего в сообщениях с клавиатуры
EmojiXpress отправлено 1.72 миллиарда, или 1720 миллионов, эмодзи. Сложите количества всех эмодзи из таблицы и сумму
поделите на 1720. Результат выведите в процентах с точностью до одного знака после запятой (уже сделано в прекоде)
"""

# Solution:

emojixpress = [
    2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0,
    4.72, 24.7, 21.7, 10.0, 118.0, 3.31, 23.1, 1.74, 4.5, 0.0333
]
emojixpress_total = 1720

# Переменная для хранения суммы
# selected_total (англ. selected total, "сумма выбранного").
selected_total = 0
for count in emojixpress:
    selected_total = selected_total + count

# Переменная для хранения доли
# selected_part (англ. selected part, "доля выбранного").
selected_part = selected_total / emojixpress_total
print('Доля выбранных эмодзи в EmojiXpress: {:.1%}'.format(selected_part))

########################################################################################################################

# 8.2 - Циклы с изменением значений переменных

"""
Задание
Посчитайте теперь, какую долю выбранные нами эмодзи составили среди отправленных в Твиттере. Всего там зарегистрировано
24.5 миллиарда или 24500 миллионов эмодзи (источник EmojiTracker, данные на конец 2018). Переменную для хранения суммы
назовите selected_total
"""

# Solution:

twitter = [
    87.3, 150, 0.0, 2270.0, 264.0, 565.0, 834.0, 432.0, 0.0, 478.0,
    198.0, 654.0, 98.7, 445.0, 1080.0, 697.0, 227.0, 0.0, 150.0, 932.0
]
twitter_total = 24500

selected_total = 0
for item in twitter:
    selected_total = selected_total + item
selected_part = selected_total / twitter_total
print('Доля выбранных эмодзи в Твиттере: {:.1%}'.format(selected_part))

########################################################################################################################

# 10.1 - Списки списков

"""
Добавьте в таблицу data еще две строки: для эмодзи «Слёзы радости» 😂 и «Подмигиваю» 😉
"""

# Solution:

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0]
]

########################################################################################################################

# 10.2 - Списки списков

"""
Задание
Используйте обращение по двойному индексу, чтобы получить из таблицы количество эмодзи «Слёзы радости» в Instagram
Напечатайте результат на экране
"""

# Solution:

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0]
]

print(data[3][2])

########################################################################################################################

# 11 - Циклы по спискам циклов

"""
Задание
Допишите код, чтобы он распечатывал всю таблицу в таком формате:

Название эмодзи | EmojiXpress, млн | Instagram, млн | Твиттер, млн
------------------------------------------------------------------
Ухмыляюсь  |  2.26  |  1.02  |  87.3
"""

# Solution:

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]

# дополните этот код:
print('Название эмодзи | EmojiXpress, млн | Instagram, млн | Твиттер, млн')
print('------------------------------------------------------------------')
for row in data:
    print(row[0], ' | ', row[1], ' | ', row[2], ' | ', row[3])

########################################################################################################################

# 12 - Выравнивание текста

"""
Задание
Допишите код, чтобы он выводил текст:

    в ячейке шириной в 15 символов
    с выравниванием по правому краю
    с заполнением пустот пробелами
"""

# Solution:

print('|{: >15}|'.format('Сердце'))

########################################################################################################################

# 12.2 - Выравнивание текста

"""
Задание
Допишите код, чтобы он выводил число:

    в ячейке шириной в 12 символов;
    с выравниванием по левому краю;
    с заполнением пустот пробелами;
    с точностью до двух знаков после запятой
"""

# Solution:

print('|{: <12.2f}|'.format(87.5))

########################################################################################################################

# 12.3 - Выравнивание текста

"""
Задание
Задача3 / 3
Обновите код вывода всей таблицы, добавив выравнивание и вывод чисел с точностью до двух знаков после запятой
Результат должен выглядеть так:

Название эмодзи  | EmojiXpress, млн | Instagram, млн | Твиттер, млн
-------------------------------------------------------------------
Ухмыляюсь        |             2.26 |           1.02 |        87.30
Сияю от радости  |            19.10 |           1.69 |       150.00
Катаюсь от смеха |            25.60 |           0.77 |         0.00   
...

Для каждого столбца подобрана такая ширина, чтобы все значения помещались. Мы уже добавили в прекод заголовок
с правильной шириной. А из этой таблицы можно получить ширины столбцов для шаблона функции format():
Столбец	Ширина
Название эмодзи	16
EmojiXpress, млн	16
Instagram, млн	14
Твиттер, млн	12
"""

# Solution:

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]


print('Название эмодзи  | EmojiXpress, млн | Instagram, млн | Твиттер, млн')
print('-------------------------------------------------------------------')
for row in data:
    # В функцию format() можно передавать несколько
    # аргументов и для каждого указывать, как его выводить.
    # Напишите код форматирования вместо многоточий.
    print('{: <16} | {: >16.2f} | {: >14.2f} | {: >12.2f}'.format(row[0], row[1], row[2], row[3]))

########################################################################################################################

# 13 - Длина строки и списка

"""
Задание
Для всех топовых эмодзи посчитайте, сколько в среднем сообщений в EmojiXpress отправляется с ними (в миллионах)
Выведите результат на экран с точностью до двух знаков после запятой
Для суммирования значений создайте переменную sum_emojixpress (англ. sum, «сумма»), а среднее сохраните в
переменной mean_emojixpress (англ. mean, здесь в значении «среднее»)
"""

# Solution:

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]

# < напишите код здесь >
sum_emojixpress = 0
for row in data:
    sum_emojixpress += row[1]
mean_emojixpress = sum_emojixpress / len(data)
print('{:.2f}'.format(mean_emojixpress))

########################################################################################################################

# 13.2 - Длина строки и списка

"""
Задание
Теперь добавьте вычисление средних значений и для остальных платформ. Сохраните результаты в переменных
mean_emojixpress, mean_instagram и mean_twitter. Код для наглядного вывода результата мы уже написали
"""

# Solution:

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]

sum_emojixpress = 0
for row in data:
    sum_emojixpress += row[1]
mean_emojixpress = sum_emojixpress / len(data)

# < напишите код здесь >
sum_instagram = 0
sum_twitter = 0
for row in data:
    sum_instagram += row[2]
    sum_twitter += row[3]
mean_instagram = sum_instagram / len(data)
mean_twitter = sum_twitter / len(data)

print('--- Средние значения ---')
print()
print('Emojixpress, млн | Instagram, млн | Твиттер, млн')
print('------------------------------------------------')
# Обратите внимание на оформление длинной строки кода. Внутри
# скобок в вызове функции можно ставить переносы строк.
print('{: ^16.2f} | {: ^14.2f} | {: ^12.2f}'.format(
    mean_emojixpress, mean_instagram, mean_twitter))

########################################################################################################################

# 14 - Анализ связи между столбцами

"""
Задание
Посчитайте для каждого эмодзи соотношение его количества в Твиттере к количеству в Instagram. Выведите результат на
экран в формате как в примере ниже. Все соотношения выводите с точностью до двух знаков после запятой

Название эмодзи          | Соотношение Твиттер/Instagram
--------------------------------------------------------
Ухмыляюсь                |                         85.59
Сияю от радости          |                           ...
...
"""

# Solution:

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]

print('Название эмодзи  | Соотношение Твиттер/Instagram')
print('------------------------------------------------')
for row in data:
    value = round(row[3] / row[2], 2)
    print('{: <16} | {: >29.2f}'.format(row[0], value))

########################################################################################################################
