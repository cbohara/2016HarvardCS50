import pandas as pd
from io import StringIO
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans


"""
Unsupervised learning example

Cluster according to topic based on IMDb synopsis
"""

# retreive google doc spreadsheet
raw_movie_data = requests.get('https://docs.google.com/spreadsheets/d/1udJ4nd9EKlX_awB90JCbKaStuYh6aVjh1X6j8iBUXIU/export?format=csv')
# convert to string for StringIO
string_movie_data = raw_movie_data.content.decode('utf-8')
frame = pd.read_csv(StringIO(string_movie_data))
# print(frame)

# push each synopsis into a list containing the string description into the larger all_synopsis matrix
all_synopsis = []
for i in range(0, frame["Synopsis"].size):
    all_synopsis.append(frame["Synopsis"][i])

# eliminate noise and account of different synopsis lengths with tf-idf matrix
# min_df = 0.2 means that the word must be in at least 20% of each synopsis
vectorizer = TfidfVectorizer(stop_words= 'english', min_df = 0.2)
x = vectorizer.fit_transform(all_synopsis)

# now run k-means algorithm to sort into clusters
k = 2
# define the proper notation distance to deal with synposis
dist = 1 - cosine_similarity(x)
# run the algorithm KMeans
model = KMeans(n_clusters = k)
model.fit(x)

# visualize outcome - print the title of the movie in each cluster, plus the top words per cluster
number_words_per_cluster = 4
# sort cluster centers by proximity to centroid
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
# array of counted words
terms = vectorizer.get_feature_names()
# get labels assigned to each data by the unsupervised algorithm
labels = model.labels_

print("Top terms per cluster:\n")
for i in range(k):
    print("Cluster " + str(i) + " movies: ")
    for title in frame["Title"][labels == i]:
        print(title)
    print()

    print("Cluster " + str(i) + " words: ")
    for index in order_centroids[i, :number_words_per_cluster]:
        print(terms[index])
    print()
