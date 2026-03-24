"""
Run this script once to generate similarity.pkl file
This is needed because the file is too large for GitHub
"""
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading movie data...")
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

print("Creating similarity matrix...")
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

print("Saving similarity.pkl...")
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✓ Done! similarity.pkl created successfully")
