########################################################################################################################
#
# 2. Первая программа
# Анализ информации начинается с вывода на экран. В Python это очень просто, давайте попробуем
#
#    Напечатайте в окне «Код» следующий текст:
#       print('Ура!')
#
# Solution:
#
print('Ура!')
#
########################################################################################################################
#
# 3. Функция print()
# Задача
# Вызовите функцию print() со следующим аргументом:
# 'Исследование распространённости языков.'
#
# Solution:
#
print('Исследование распространённости языков.')
#
########################################################################################################################
#
# 4. Операции с числами
#
# Python умеет оперировать числами как обычный калькулятор. Для анализа мы взяли список языков, на которых написано не
# менее 100 тысяч сайтов из 10 миллионов самых посещаемых в интернете. Давайте посчитаем суммарное количество
# носителей всех славянских языков из выбранных: русского, польского и чешского языков в миллионах:
# Язык	Носители языка, млн
# Английский	378.2
# Русский	153.9
# Немецкий	76.0
# Испанский	442.3
# Французский	76.7
# Японский	128.2
# Португальский	222.7
# Итальянский	64.8
# Персидский	60.0
# Польский	39.6
# Китайский	908.7
# Датский	22.0
# Турецкий	78.5
# Чешский	10.4
# Источник: Ethnologue (издание 2018 года
#
# Напишите на Python программу, которая печатает на экране суммарное количество носителей романских языков: испанского,
# французского, португальского и итальянского языков в миллионах. Значения из таблицы внесите в код вручную
#
# Solution:
#
print(442.3 + 76.7 + 222.7 + 64.8)
#
########################################################################################################################
#
# 5. Умножение, деление, вычитание
#
# Аналитик может получить неожиданный результат даже расчётом на калькуляторе. Сравним, к примеру, распространённость
# языков на Земле с их местом в интернете. Специально для вас мы подготовили сравнение количества владеющих языком
# и доли сайтов на этом языке среди 10 миллионов самых популярных сайтов в интернете вообще
#
# Язык	Доля сайтов в топ-10 млн	Носители языка, млн чел.	Все владеющие языком, млн чел.
# Английский	0.539	378.2	1121.0
# Русский	0.061	153.9	264.3
# Немецкий	0.060	76.0	132.0
# Испанский	0.049	442.3	512.9
# Французский	0.040	76.7	284.9
# Японский	0.034	128.2	128.3
# Португальский	0.029	222.7	236.5
# Итальянский	0.024	64.8	67.8
# Персидский	0.020	60.0	110.0
# Польский	0.018	39.6	40.3
# Китайский	0.017	908.7	1107.0
# Датский	0.012	22.0	28.0
# Турецкий	0.012	78.5	78.9
# Чешский	0.010	10.4	10.6
#
# Вычислите, сколько людей выучили русский язык как иностранный (в миллионах). Напечатайте результат на экране
#
# Solution:
#
print(264.3 - 153.9)
#
########################################################################################################################
#
# 6. Порядок операций
#
# Теперь используем скобки, чтобы посчитать долю выучивших английский язык как иностранный среди всех, кто на нём
# говорит:
#
# Язык	Доля сайтов в топ-10 млн	Носители языка, млн	Все владеющие языком, млн
# Английский	0.539	378.2	1121.0
# Русский	0.061	153.9	264.3
# Немецкий	0.060	76.0	132.0
# Испанский	0.049	442.3	512.9
# Французский	0.040	76.7	284.9
# Японский	0.034	128.2	128.3
# Португальский	0.029	222.7	236.5
# Итальянский	0.024	64.8	67.8
# Персидский	0.020	60.0	110.0
# Польский	0.018	39.6	40.3
# Китайский	0.017	908.7	1107.0
# Датский	0.012	22.0	28.0
# Турецкий	0.012	78.5	78.9
# Чешский	0.010	10.4	10.6
#
# print((1121 - 378.2) / 1121) // 0.6626226583407672
#
# Посчитайте, какую долю среди владеющих японским языком составляют те, кто выучил его как иностранный. Напечатайте
# результат на экране
#
# Solution:
#
print((128.3 - 128.2) / 128.3)
#
########################################################################################################################
#
# 7. Комментарии
#
# Выполните описанные в комментарии вычисления и напечатайте результат на экране
#
# Solution:
#
# Посчитайте, во сколько раз число носителей китайского языка больше
# числа носителей английского. Напечатайте результат на экране.
print(908.7 / 378.2) # напишите код вместо многоточия
#
########################################################################################################################
#
# 9. Переменные
#
# Язык	Доля сайтов в топ-10 млн	Носители языка, млн	Все владеющие языком, млн
# Английский	0.539	378.2	1121.0
# Русский	0.061	153.9	264.3
# Немецкий	0.060	76.0	132.0
# Испанский	0.049	442.3	512.9
# Французский	0.040	76.7	284.9
# Японский	0.034	128.2	128.3
# Португальский	0.029	222.7	236.5
# Итальянский	0.024	64.8	67.8
# Персидский	0.020	60.0	110.0
# Польский	0.018	39.6	40.3
# Китайский	0.017	908.7	1107.0
# Датский	0.012	22.0	28.0
# Турецкий	0.012	78.5	78.9
# Чешский	0.010	10.4	10.6
#
# Давайте выясним, кого больше — носителей китайского языка или вместе взятых носителей трёх самых популярных в
# интернете языков. Объявите переменную top3_total и запишите в неё суммарное количество носителей английского,
# русского и немецкого языков. Вычтите полученное значение из количества носителей китайского языка и выведите
# результат на экран. Используйте переменные из прошлой задачи
#
# Solution:
#
english = 378.2
russian = 153.9
german = 76.0
chinese = 908.7
# < напишите код здесь >
top3_total = english + russian + german
print(chinese - top3_total)
#
########################################################################################################################
#
# 10. Использование переменных
#
# Язык	Доля сайтов в топ-10 млн	Носители языка, млн	Все владеющие языком, млн
# Английский	0.539	378.2	1121.0
# Русский	0.061	153.9	264.3
# Немецкий	0.060	76.0	132.0
# Испанский	0.049	442.3	512.9
# Французский	0.040	76.7	284.9
# Японский	0.034	128.2	128.3
# Португальский	0.029	222.7	236.5
# Итальянский	0.024	64.8	67.8
# Персидский	0.020	60.0	110.0
# Польский	0.018	39.6	40.3
# Китайский	0.017	908.7	1107.0
# Датский	0.012	22.0	28.0
# Турецкий	0.012	78.5	78.9
# Чешский	0.010	10.4	10.6
#
# В этом примере мы анализируем данные за 2018 год. Если нужно узнать положение на 2013-й, мы можем просто подставить
# новые значения переменных
#
#     Доля англоязычных сайтов на 2013 год: 0.549
#     Доля русскоязычных сайтов на 2013 год: 0.055
#
# english = 0.549
# russian = 0.055
# print(english / russian) // 9.981818181818182
# Как видите, доля сайтов с русским языком за 5 лет выросла
#
# Программа делит друг на друга доли сайтов на японском и на китайском языках в 2018 году. Подставьте в те же переменные
# значения на 2013 год (см. ниже)
#     Доля сайтов на японском языке за 2013 год: 0.045
#     Доля сайтов на китайском языке за 2013 год: 0.043
#
# Solution:
#
japanese = 0.045
chinese = 0.043
print(chinese / japanese)
#
########################################################################################################################
#
# 11. Типы данных
#
# Мы добавили переменные в программу, которая вычисляла количество русскоязычных сайтов, вошедших в 10 миллионов самых
# популярных. Давайте посмотрим на полученный код. Если переменная russian_web_part имеет тип float, а переменная
# web_popular имеет тип int, какой тип должен быть у переменной russian_web_popular?
# Напечатайте на отдельных строках:
#
#     Значение переменной.
#     Тип переменной (вызовом функции type())
#
# Solution:
#
russian_web_part = 0.061
web_popular = 10000000

russian_web_popular = russian_web_part * web_popular
print(russian_web_popular)
print(type(russian_web_popular))
#
########################################################################################################################
#
# 12. Преобразования типов
#
# Мы написали код, преобразующий количество носителей русского языка в млн (переменная russian_native_millions) в
# количество носителей русского языка в чел. (переменная russian_native). Вторая переменная преобразована к типу int,
# так как в ней лежит количество человек. Вызов функции int() организован неудачно: теряется 900 тыс. человек. Измените
# код так, чтобы в переменной russian_native оказалось значение типа int, и никто не потерялся
#
# Solution:
#
russian_native_millions = 153.9
russian_native = int(russian_native_millions * 1000000)
print(russian_native)
#
########################################################################################################################
#
# 13. Ошибки
#
# Задача
# В этом задании вы можете поэкспериментировать с разными ошибками и посмотреть на сообщения о них. По очереди скрывайте
# строчки с неверным кодом «решётками» — помните, что значит «закомментировать»? Cообщения об ошибках выдает не наш
# тренажёр, а сам Python. Когда наэкспериментируетесь, удалите весь код (тренажёр не пропускает код с ошибками),
# и нажимайте кнопку тренажёра «Проверить», чтобы попасть в следующий урок
#
########################################################################################################################
#
# 14. Языки в оффлайне и в онлайне
#
# Задача
# Сначала занесем все необходимые величины из таблицы в переменные. Для удобства все вычисления будем производить в
# миллионах. Объявите следующие переменные:
#
#     chinese_speakers для количества людей, говорящих на китайском языке;
#     chinese_web_part для доли сайтов с китайским языком;
#     и по аналогии – переменные english_speakers, english_web_part, russian_speakers, russian_web_part.
#
# Население планеты и число сайтов мы уже заполнили
#
# Solution:
#
total_web = 10
total_speakers = 7539

chinese_speakers = 1107.0# < напишите код здесь >
chinese_web_part = 0.017# < напишите код здесь >

english_speakers = 1121.0
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061
#
########################################################################################################################
#
# 15. Печать на одной строке
#
# Вычислите долю людей, говорящих на китайском языке. Присвойте это значение переменной chinese_speakers_part
# Напечатайте значение на экране в таком формате:
#
# Доля людей, говорящих на китайском: ...
#
# Сделайте так же для английского и русского языков. Переменные назовите english_speakers_part и russian_speakers_part
# соответственно
#
# Solution:
#
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
print('Доля людей, говорящих на китайском:', chinese_speakers_part) # напишите код вместо многоточия

english_speakers_part = (english_speakers / total_speakers)
print('Доля людей, говорящих на английском:', english_speakers_part)

russian_speakers_part = (russian_speakers / total_speakers)
print('Доля людей, говорящих на русском:', russian_speakers_part)
#
########################################################################################################################
#
# 16. Функция format()
#
# Результат печати функции в предыдущем уроке пока оставляет желать лучшего:
#
#     Python напечатал слишком много цифр после запятой.
#     Доли нагляднее показывать в процентах.
#
# Такие проблемы решает функция format()
#
# Задача 1:
# Создайте переменную chinese_native с числом носителей китайского языка и напечатайте эту величину на экране
# в таком виде:
#
# Китайский язык - родной для ... млн человек
#
# Воспользуйтесь функцией format()
#
# Solution:
#
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

chinese_speakers_part = chinese_speakers / total_speakers
print('Китайский язык - родной для {} млн человек'.format())(chinese_speakers_part)
#
# Задача 2:
# Вернёмся к задаче, с которой мы начали — вычислению доли владеющих разными языками среди всего населения Земли
# Напечатайте на экране долю говорящих на китайском, сопровождая текстом:
#
# Доля людей, говорящих на китайском: ...
#
# Solution:
#
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

chinese_speakers_part = chinese_speakers / total_speakers
print('Доля людей, говорящих на китайском: {:.2f}'.format(chinese_speakers_part)) # напишите код вместо многоточия
#
# Задача 3:
# Теперь напечатайте на экране долю людей, говорящих на китайском языке, в процентах вот в таком виде:
#
# Доля людей, говорящих на китайском: ...
#
# Выведите результат с точностью до одного знака после запятой. Напечатайте аналогичные величины для английского
# и русского языков
#
# Solution:
#
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
english_speakers_part = english_speakers / total_speakers
russian_speakers_part = russian_speakers / total_speakers
print('Доля людей, говорящих на китайском: {:.1%}' .format(chinese_speakers_part))
print('Доля людей, говорящих на английском: {:.1%}' .format(english_speakers_part))
print('Доля людей, говорящих на русском: {:.1%}' .format(russian_speakers_part))
#
########################################################################################################################
#
# 17. Оформление текста
#
# Добавьте для каждого блока заголовок с названием языка и пустую строку после каждого блока. Уберите названия языков
# и слово «людей» из строк с долями. Вот так должен выглядеть ваш вывод:
#
# --- Китайский язык ---
# Доля говорящих на языке: ...
#
# --- Английский язык ---
# Доля говорящих на языке: ...
#
# --- Русский язык ---
# Доля говорящих на языке: ...
#
# Solution:
#
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
print('--- Китайский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(chinese_speakers_part))
print()

english_speakers_part = english_speakers / total_speakers
print('--- Английский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(english_speakers_part))
print()

russian_speakers_part = russian_speakers / total_speakers
print('--- Русский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(russian_speakers_part))
print()
#
########################################################################################################################
#
# 18. Языки в оффлайне и в онлайне: завершение
#
# Теперь, вооружившись функциями print() и format(), представим результаты исследования эффектно. Тем более, нам есть
# что подать: сейчас мы вычислим степень цифровой активности каждого языка — тот самый «индекс проникновения
# в интернет»
#
# Добавьте в каждый блок информацию о доле сайтов на соответствующем языке. Долю напечатайте в процентах с точностью
# до 1 знака после запятой. Вывод должен выглядеть так:
#
# --- Китайский язык ---
# Доля говорящих на языке: ...
# Доля сайтов с языком: ...
#
# --- Английский язык ---
# Доля говорящих на языке: ...
# Доля сайтов с языком: ...
#
# --- Русский язык ---
# Доля говорящих на языке: ...
# Доля сайтов с языком: ...
#
# Solution:
#
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
print('--- Китайский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(chinese_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(chinese_web_part))
print()

english_speakers_part = english_speakers / total_speakers
print('--- Английский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(english_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(english_web_part))
print()

russian_speakers_part = russian_speakers / total_speakers
print('--- Русский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(russian_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(russian_web_part))
#
# Задача 2:
#
# Задача2 / 2
# Добавим в каждый блок информацию об индексе проникновения в интернет. Поделим число сайтов с языком на число людей,
# которые на нём говорят. Для наглядности умножьте результат на 1000 и выведите с точностью до двух знаков после
# запятой. Итог должен выглядеть так:
#
# --- Китайский язык ---
# Доля говорящих на языке: ...
# Доля сайтов с языком: ...
# Индекс проникновения в интернет: ...
#
# --- Английский язык ---
# Доля говорящих на языке: ...
# Доля сайтов с языком: ...
# Индекс проникновения в интернет: ...
#
# --- Русский язык ---
# Доля говорящих на языке: ...
# Доля сайтов с языком: ...
# Индекс проникновения в интернет: ...
#
# Solution:
#
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
chinese_web_sites = chinese_web_part * total_web
chinese_index = 1000 * chinese_web_sites / chinese_speakers
print('--- Китайский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(chinese_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(chinese_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(chinese_index))
# < напишите код здесь >
print()

english_speakers_part = english_speakers / total_speakers
english_web_sites = english_web_part * total_web
english_index = 1000 * english_web_sites / english_speakers
# < напишите код здесь >
print('--- Английский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(english_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(english_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(english_index))
# < напишите код здесь >
print()

russian_speakers_part = russian_speakers / total_speakers
russian_web_sites = russian_web_part * total_web
russian_index = 1000 * russian_web_sites / russian_speakers
# < напишите код здесь >
print('--- Русский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(russian_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(russian_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(russian_index))
# < напишите код здесь >
print()
# 
########################################################################################################################
