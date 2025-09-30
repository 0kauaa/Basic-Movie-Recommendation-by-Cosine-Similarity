# libs
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# dataset
movies = pd.read_csv("")

# movies.info()
"""""""""
INFO DO DATASET UTILIZADO

RangeIndex: 14828 entries, 0 to 14827
Data columns (total 6 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   imdb_id          14828 non-null  object
 1   title            14828 non-null  object
 2   plot_synopsis    14828 non-null  object
 3   tags             14828 non-null  object
 4   split            14828 non-null  object
 5   synopsis_source  14828 non-null  object
dtypes: object(6)
memory usage: 695.2+ KB
None
"""""""""

# colunas utilizadas
title = movies['title'].str.lower()
plot = movies['plot_synopsis']
genre = movies['tags']

# tfidf
vectorizer = TfidfVectorizer(stop_words='english')
PlotVector = vectorizer.fit_transform(plot)

# verificação da existência do filme
while True:
    movie = input("Insira um filme que te interessa: ").strip().lower()

    if movie in title.values:
        n = int(input("Insira quantas recomendações deseja: "))
        idx = title[title == movie].index[0]
        break

    else:
        print(f"Desculpe, o filme {movie} não foi encontrado. Tente novamente.")

# similaridade
similarity = cosine_similarity(PlotVector[idx], PlotVector)

# n fimlmes mais similares, exceto o próprio
similar_movies = similarity.argsort()[0][-n-1:-1][::-1]

# recomendação e saída
def byplot(similar_movies):

    if len(similar_movies) == 0:
        print(f"Desculpe, não foi encontrado nenhum filme similar a {movie}.")        

    else:
        for i, index in enumerate(similar_movies):
            print(f"\nFilme recomendado {i+1}: {title.iloc[index]}.")
            print(f"Genêro: {genre.iloc[index]}.")
            print(f"Sinopse: {plot.iloc[index]}.")

byplot(similar_movies)
