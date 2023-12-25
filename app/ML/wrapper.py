import os
import pickle

class MovieRatingPrediction():
    def __init__(self):
        with open(r"models/pickle_model.pkl", 'rb') as file:
            self.model = pickle.load(file)
        with open(r"models/pickle_vectorizer.pkl", 'rb') as file:
            self.cv = pickle.load(file)

    def predict(self, data): 
        Vec = self.cv.transform([data]).toarray()
        return self.model.predict(Vec)