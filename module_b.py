# import matplotlib.pyplot as plt
# import seaborn as sb
# import pandas as pd
#
# file = pd.read_excel('./Книга1.xlsx')
# file['Дата публикации'] = pd.to_datetime(file['Дата публикации'])
#
# plt.figure(figsize=(12, 8))
# median_salaries_by_region = file.groupby('Регион')['Зарплата'].median().nlargest(10)
# sb.barplot(x=median_salaries_by_region.values, y=median_salaries_by_region.index)
# plt.title('Топ-10 регионов по медианной зарплате')
# plt.xlabel('Медианная зарплата')
# plt.ylabel('Регион')
# plt.show()
#
# plt.figure(figsize=(12, 6))
# file['Месяц_публикации'] = file['Дата публикации'].dt.to_period('M')
# publications_by_month = file.groupby('Месяц_публикации').size()
# publications_by_month.plot(kind='line', marker='o')
# plt.title('Динамика публикаций вакансий по месяцам')
# plt.xlabel('Месяц публикации')
# plt.ylabel('Количество публикаций')
# plt.xticks(rotation=45)
# plt.show()
#
# plt.figure(figsize=(8, 6))
# sb.countplot(y='Опыт работы', data=file, order=file['Опыт работы'].value_counts().index)
# plt.title('Распределение вакансий по требуемому опыту работы')
# plt.xlabel('Количество вакансий')
# plt.ylabel('Опыт работы')
# plt.show()
#
# plt.figure(figsize=(8, 6))
# sb.countplot(y='График', data=file, order=file['График'].value_counts().index)
# plt.title('Распределение вакансий по графику работы')
# plt.xlabel('Количество вакансий')
# plt.ylabel('График работы')
# plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Читаем данные
df = pd.read_excel('./Книга1.xlsx')
df['Дата публикации'] = pd.to_datetime(df['Дата публикации'])
df['Месяц_публикации'] = df['Дата публикации'].dt.to_period('M')

# Настройка размера фигуры для всей страницы
plt.figure(figsize=(15, 10))

# Первый подграфик
plt.subplot(2, 2, 1)  # 2 строки, 2 столбца, позиция 1
median_salaries_by_region = df.groupby('Регион')['Зарплата'].median().nlargest(10)
sns.barplot(x=median_salaries_by_region.values, y=median_salaries_by_region.index)
plt.title('Топ-10 регионов по медианной зарплате')
plt.xlabel('Медианная зарплата')
plt.ylabel('Регион')

# Второй подграфик
plt.subplot(2, 2, 2)  # 2 строки, 2 столбца, позиция 2
publications_by_month = df.groupby('Месяц_публикации').size()
publications_by_month.plot(kind='line', marker='o')
plt.title('Динамика публикаций вакансий по месяцам')
plt.xlabel('Месяц публикации')
plt.ylabel('Количество публикаций')
plt.xticks(rotation=45)

# Третий подграфик
plt.subplot(2, 2, 3)  # 2 строки, 2 столбца, позиция 3
sns.countplot(y='Опыт работы', data=df, order=df['Опыт работы'].value_counts().index)
plt.title('Распределение вакансий по требуемому опыту работы')
plt.xlabel('Количество вакансий')
plt.ylabel('Опыт работы')

# Четвертый подграфик
plt.subplot(2, 2, 4)  # 2 строки, 2 столбца, позиция 4
sns.countplot(y='График', data=df, order = df['График'].value_counts().index)
plt.title('Распределение вакансий по графику работы')
plt.xlabel('Количество вакансий')
plt.ylabel('График работы')

# Автоматическая корректировка подписей и отступов
plt.tight_layout()
# Отображение всех графиков
plt.show()
