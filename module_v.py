import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# Загрузите данные описаний вакансий
job_descriptions = pd.read_excel('./Книга1.xlsx')

# Токенизуйте описания вакансий
tokenized_descriptions = job_descriptions['Описание вакансии'].apply(word_tokenize)

# Приводим токены к нижнему регистру
tokenized_descriptions = tokenized_descriptions.apply(lambda x: [word.lower() for word in x])

# Удалите стоп-слова
stop_words = set(stopwords.words('russian'))
tokenized_descriptions = tokenized_descriptions.apply(lambda x: [word for word in x if word not in stop_words])

# Извлеките навыки из токенизованных описаний
skills = [word for tokens in tokenized_descriptions for word in tokens]

# Группируйте похожие навыки вместе с помощью Counter
skill_counts = Counter(skills)

# Определите популярность каждой группы навыков на основе частоты упоминания
skill_popularity = pd.DataFrame({'Навык': list(skill_counts.keys()), 'Частота': list(skill_counts.values())})

# Сортируйте навыки по частоте в порядке убывания
skill_popularity = skill_popularity.sort_values('Частота', ascending=False)

# Экспортируйте результаты в таблицу Excel
skill_popularity.to_excel('навыки_популярность.xlsx', index=False)

# Создаем объект TF-IDF
vectorizer = TfidfVectorizer()

# Векторизуем текстовые данные
skill_vectors = vectorizer.fit_transform(skill_popularity['Навык'])

# Создаем матрицу признаков для навыков
skill_matrix = skill_vectors.toarray()

# Создаем объект KMeans
kmeans = KMeans(n_clusters=5)

# Обучаем модель на матрице признаков
kmeans.fit(skill_matrix)

# Получаем метки кластеров для каждого навыка
labels = kmeans.labels_

# Создаем новый столбец в таблице навыков для меток кластеров
skill_popularity['Кластер'] = labels

# Группируем навыки по кластерам
grouped_skills = skill_popularity.groupby('Кластер')['Навык'].apply(lambda x: ', '.join(x))

# Выводим результаты
print(grouped_skills)
