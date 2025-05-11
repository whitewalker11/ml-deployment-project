import pickle
from sklearn.linear_model import LogisticRegression

def train_model():
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    model = LogisticRegression().fit(X, y)
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model()
