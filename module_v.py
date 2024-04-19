import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter


stop_words = set(stopwords.words('russian'))
df = pd.read_excel('./Книга1.xlsx')


# Функция для предварительной обработки и извлечения навыков
def extract_skills(description):
    tokens = word_tokenize(description.lower())
    skills = [token for token in tokens if token.isalpha() and token not in stop_words]
    return skills


# Применяем функцию к каждой записи в столбце "Описание"
df['Навыки'] = df['Описание вакансии'].apply(extract_skills)

# Собираем все навыки в один список и подсчитываем частоту встречаемости каждого навыка
all_skills = sum(df['Навыки'].tolist(), [])
skills_frequency = Counter(all_skills)

# Создаем DataFrame с навыками и их частотой встречаемости
skills_df = pd.DataFrame(skills_frequency.items(), columns=['Навык', 'Частота']).sort_values(by='Частота', ascending=False)

# Сохраняем результаты в Excel
skills_df.to_excel('./описание_навыков.xlsx', index=False)
