from modules.model import vectorizer, model_predict
from flask import Blueprint, request, Response
import json


model_blueprint = Blueprint("sentiment_analysis_model", __name__)


@model_blueprint.route("/model_predict", methods=["POST"])
def predictions():
    try:
        data = request.get_json()
        text = data["text"]
        vector = vectorizer([text], "vector.pkl")
        prediction = str(model_predict(vector=vector, path_to_model="model.pkl")[0])
        if prediction == "1":
            prediction = "Positive"
        else:
            prediction = "Negative"
        response_data = {"data": prediction, "message": True}
        return Response(json.dumps(response_data), 200)
    except Exception as e:
        response_data = {"data": f"{str(e)}", "message": False}
        return Response(json.dumps(response_data), 500)
