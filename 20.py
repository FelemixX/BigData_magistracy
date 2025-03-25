import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic/test.csv')

print("Первые 5 строк данных:")
print(df.head())

print("\nИнформация о данных:")
print(df.info())

print("\nОписательная статистика:")
print(df.describe())

print("\nКоличество пропущенных значений в каждом столбце:")
print(df.isnull().sum())


# Распределение возраста пассажиров
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'].dropna(), bins=20, kde=True, color='skyblue')
plt.title('Распределение возраста пассажиров')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

# Распределение выживаемости
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Survived', palette='pastel')
plt.title('Распределение выживаемости')
plt.xlabel('Выжил (0 - Нет, 1 - Да)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

# Влияние пола на выживаемость
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Survived', hue='Sex', palette='pastel')
plt.title('Влияние пола на выживаемость')
plt.xlabel('Выжил (0 - Нет, 1 - Да)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

# Влияние класса на выживаемость
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Pclass', hue='Survived', palette='pastel')
plt.title('Влияние класса на выживаемость')
plt.xlabel('Класс (1 - Высший, 2 - Средний, 3 - Нижний)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

# Выявление выбросов
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Age'])
plt.title('Боксплот для возраста')
plt.grid(True)
plt.show()

# Корреляции между числовыми признаками
correlation_matrix = df.corr()

# Тепловая карта корреляций
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Корреляции между числовыми признаками')
plt.show()

# Заполнение пропущенных значений медианой для числовых колонок
df['Age'].fillna(df['Age'].median(), inplace=True)

# Заполнение пропущенных значений наиболее частым значением для категориальных колонок
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

print("\nКоличество пропущенных значений после обработки:")
print(df.isnull().sum())