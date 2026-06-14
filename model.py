import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# load dataset
data = pd.read_csv("dataset.csv")

# input and output
X = data["command"]
y = data["intent"]

# convert text to numbers
vectorizer = CountVectorizer()

X_vectors = vectorizer.fit_transform(X)

# train model
model = MultinomialNB()

model.fit(X_vectors, y)

# test
test = ["open youtube"]

test_vector = vectorizer.transform(test)

prediction = model.predict(test_vector)

print(prediction)