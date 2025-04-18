Задания на ознакомление с библиотекой Pandas
1. Создание DataFrame
Создайте DataFrame из словаря, где ключи — названия колонок, а значения — списки
данных.
2. Чтение CSV
Загрузите CSV-файл с данными (например, Titanic Dataset) и выведите первые 5 строк.
3. Базовые операции
Для загруженного DataFrame выведите: количество строк/столбцов, названия колонок,
типы данных.
4. Фильтрация данных
Выберите строки, где значение в определённой колонке (например, "Age") больше
заданного числа.
5. Выбор столбцов
Выведите только два определённых столбца из DataFrame.
6. Добавление столбца
Создайте новый столбец на основе существующих данных (например, "Age_in_Days" = Age
* 365).
7. Группировка и агрегация
Сгруппируйте данные по категориальной колонке (например, "Sex") и посчитайте среднее
значение числовой колонки (например, "Fare").
8. Сортировка
Отсортируйте DataFrame по убыванию значений в определённой колонке.
9. Обработка пропусков
Проверьте DataFrame на наличие пропущенных значений и заполните их
средним/медианным значением.
10. Объединение DataFrame
Создайте два DataFrame и объедините их вертикально (concat) и горизонтально (merge).
11. Применение функций
Используйте метод .apply() для преобразования значений в колонке (например, перевод
строк в верхний регистр).
12. Работа с датами
Конвертируйте строковую колонку с датами в тип datetime и извлеките месяц/год.
13. Pivot Table
Создайте сводную таблицу с помощью pivot_table() для анализа данных.
14. Удаление дубликатов
Найдите и удалите полностью дублирующиеся строки.
15. Работа с индексами
Сбросьте индекс и установите другую колонку в качестве нового индекса.
16. Фильтр по строковым значениям
Отберите строки, где текст в колонке содержит определенную подстроку
(метод .str.contains()).
17. Категориальные данные
Конвертируйте текстовую колонку в категориальный тип и посчитайте частоты значений.
18. Сохранение данных
Отфильтруйте и обработайте DataFrame, затем сохраните результат в новый CSV-файл.
19. Временные ряды
Для данных с датами посчитайте скользящее среднее за определенный период.
20. Всесторонний анализ данных с помощью Pandas
Проведите полный EDA (анализ данных): статистика, визуализация (с помощью .plot()),
выявление аномалий и закономерностей.
21. Группировка с несколькими агрегациями
Сгруппируйте данные по двум колонкам и примените разные агрегирующие функции к
разным числовым колонкам (например, среднее к "Age", сумму к "Fare").
Пример:
df.groupby(['Col1', 'Col2']).agg({'Age': 'mean', 'Fare': 'sum'})
22. Фильтрация групп
Сгруппируйте данные по колонке и отфильтруйте группы, где среднее значение числовой
колонки превышает заданный порог (например, оставить только группы с средним
возрастом > 30 лет).
Пример:
df.groupby('GroupCol').filter(lambda x: x['Age'].mean() > 30)
23. Трансформация внутри групп
С помощью groupby и transform создайте новый столбец, содержащий нормализованные
значения внутри каждой группы (например, отклонение от среднего в группе).
Пример:
df['Normalized'] = df.groupby('GroupCol')['ValueCol'].transform(lambda x: x - x.mean())
24. Подсчёт уникальных значений в группах
Сгруппируйте данные по категориальной колонке и посчитайте количество уникальных
значений в другой колонке для каждой группы.
Пример:
df.groupby('CategoryCol')['UniqueCol'].nunique()
25. Кастомные агрегации через функции
Напишите свою функцию для агрегации (например, разницу между максимальным и
минимальным значением) и примените её к группам.
Пример:
def custom_agg(series):
return series.max() - series.min()
df.groupby('GroupCol')['ValueCol'].agg(custom_agg)
