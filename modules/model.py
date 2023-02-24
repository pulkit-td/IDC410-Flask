import pickle
from typing import List
import scipy
import numpy


def vectorizer(
    docs: List[str], path_to_model: str
) -> scipy.sparse.csr.csr_matrix:
    """
    Converts a list of raw text into a csr matrix output of CountVectorizer.

    Args:
        docs (List[str]): List of raw text.
        path_to_model (str): path to model.

    Returns:
        scipy.sparse.csr.csr_matrix
    """
    vec = pickle.load(open(path_to_model, "rb"))
    return vec.transform(docs)


def model_predict(
    vector: scipy.sparse.csr.csr_matrix, path_to_model: str
) -> numpy.ndarray:
    """
    Return prediction of the model.

    Args:
        vector (scipy.sparse.csr.csr_matrix)
        path_to_model (str): path to model.

    Returns:
        numpy.ndarray
    """
    model = pickle.load(open(path_to_model, "rb"))
    return model.predict(vector)


if __name__ == "__main__":
    v = vectorizer(["This is good"], "vector.pkl")
    print(model_predict(v, "model.pkl"))
