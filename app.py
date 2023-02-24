from flask import Flask, Response, request
from blueprints.model_api import model_blueprint
import json

app = Flask(__name__)
app.register_blueprint(model_blueprint)


@app.route("/health_check", methods=["GET"])
def health_check():

    response_data = {"data": "OK", "message": True}

    return Response(json.dumps(response_data), 200)


@app.route("/post_request", methods=["POST"])
def post_request():
    try:
        data = request.get_json()
        name = data["name"]
        email = data["email"]
        phone = data["phone"]

        operations = {
            "name": name.lower(),
            "email": email.lower(),
            "phone": int(phone),
        }

        response_data = {"data": operations, "message": True}

        return Response(json.dumps(response_data), 200)

    except Exception as e:

        response_data = {"data": f"{str(e)}", "message": False}

        return Response(json.dumps(response_data), 500)


@app.route("/get_request", methods=["GET"])
def get_request():
    try:
        data = request.args
        human = data["human"]
        if bool(human):
            response_data = {"data": "Yes", "message": True}
        else:
            response_data = {"data": "No", "message": True}

        return Response(json.dumps(response_data), 200)

    except Exception as e:

        response_data = {"data": f"{str(e)}", "message": False}

        return Response(json.dumps(response_data), 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
