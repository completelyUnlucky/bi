import itertools
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('./Книга1.xlsx')
# vacancies = [[i.lower()][0].split(", ") for i in df['Требования']]
vacancies = df['Требования'].str.lower().str.split(", ")


# Создание матрицы сопутствия
co_occurrence_dict = defaultdict(int)
for vacancy in vacancies:
    skills = sorted(vacancy)  # Сортируем навыки для последовательного исключения дубликатов
    for (skill_a, skill_b) in itertools.combinations(skills, 2):
        co_occurrence_dict[(skill_a, skill_b)] += 1

# Создание графа с использованием NetworkX
G = nx.Graph()
for (skill_a, skill_b), weight in co_occurrence_dict.items():
    if weight > 0:  # Добавляем ребро, если навыки упоминались вместе
        G.add_edge(skill_a, skill_b, weight=weight)

# Расчет метрик графа
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# Визуализация графа
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)  # Расположение узлов

# Ребра
nx.draw_networkx_edges(G, pos, alpha=0.3)

# Названия навыков
nx.draw_networkx_labels(G, pos)

# Узлы с размером, основанным на степени центральности
node_size = [v * 10000 for v in degree_centrality.values()]
nx.draw_networkx_nodes(G, pos, node_size=node_size)

# Отображение графика
plt.axis('off')
plt.show()

print("Степень центральности:", degree_centrality)
print("Центральность по посредничеству:", betweenness_centrality)
print("Теснота связей:", closeness_centrality)
