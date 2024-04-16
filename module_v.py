import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

df = pd.read_excel('./Книга1.xlsx')


def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if not token in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized)


df['processed_description'] = df['Описание вакансии'].apply(preprocess_text)

# Создание векторов TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)
tfidf_matrix = vectorizer.fit_transform(df['processed_description'])

# Кластеризация
kmeans = KMeans(n_clusters=5)
kmeans.fit(tfidf_matrix)
df['cluster'] = kmeans.labels_

# Можно провести анализ частотности навыков в разных кластерах
skill_clusters = df.groupby('cluster')['processed_description'].apply(lambda descriptions: nltk.FreqDist([skill for description in descriptions for skill in description]))


# Анализ зависимости зарплаты от навыков
df['average_salary'] = pd.to_numeric(df['Зарплата'], errors='coerce') # конвертация в числовой тип данных
highly_paid_skills = df.groupby('processed_description')['average_salary'].mean().sort_values(ascending=False)

# Анализ регионального спроса на навыки
regional_skills_demand = df.groupby('Регион')['processed_description'].apply(lambda descriptions: nltk.FreqDist([skill for description in descriptions for skill in description]))

sns.barplot(x=highly_paid_skills.values[:10], y=highly_paid_skills.index[:10])
plt.show()
