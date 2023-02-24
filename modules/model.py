import pickle
from typing import List


def vectorizer(docs:List[str], path_to_model:str):
    vec = pickle.load(open(path_to_model, 'rb'))
    return vec.transform(docs)

def model_predict(vector, path_to_model:str):
    model = pickle.load(open(path_to_model, 'rb'))
    return model.predict(vector)

if __name__ == '__main__':
    v = vectorizer(['This is good'], 'vector.pkl')
    print(model_predict(v, 'model.pkl'))