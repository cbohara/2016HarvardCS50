import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans

"""
Unsupervised learning example

Text content will be split into most-similar clusters.

First, we build a vocabulary from the words used in the text, when we do
not consider the so-called "stop words" such as "a," "the," or "in," as they do
not convey meaningful information.

For each text instance we count the number of occurrences of each word and store it into a matrix.
In the matrix, each row represents a text instance and each column represents a word.

To avoid these potential discrepancies we can divide the number of occurrences of
each word in a document by the total number of words in the document,
so that we get a frequency matrix.

Another refinement is to have downscale weights for words that occur in many
documents in the text, as these words tend to be less informative than those that
occur only in a smaller portion of the text.

The final weighted frequency matrix, is tipically called tf–idf for
“Term Frequency times Inverse Document Frequency”.
"""

sentences = ['I love CS50. Staff is awesome, awesome, awesome!',
            'I have a dog and a cat.',
            'Best of CS50? Staff. And cakes. Ok, CS50 staff.',
            'My dog keeps chasing my cat. Dogs!']

# create word count matrix
count_vect = CountVectorizer(stop_words = 'english')
z = count_vect.fit_transform(sentences)
# generate the matrix
z.todense()

# the vocab words that have been counted in the matrix
vocab = count_vect.get_feature_names()
# print(vocab)

# create tf–idf matrix
vectorizer = TfidfVectorizer(stop_words = 'english')
x = vectorizer.fit_transform(sentences)
x.todense()

# define the number of clusters
k = 2
# define the proper notation of distance to deal with input
dist = 1 - cosine_similarity(x)
# run the KMeans algorithm
model = KMeans(n_clusters = k)
model.fit(x)

print("Top terms per cluster:\n")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(k):
    print("Cluster %i:" % i, end='')
    for index in order_centroids[i, :3]:
        print(" %s, " % terms[index], end='')
    print("")
