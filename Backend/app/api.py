from flask import Flask, request, jsonify
from ia import classify_and_reply

app = Flask(__name__)

@app.route("/ping")
def ping():
    return {"status": "ok"}

@app.route("/classificar", methods=["POST"])
def classificar():
    data = request.get_json()
    email = data.get("email", "")

    if not email:
        return jsonify({"erro": "Email vazio"}), 400

    result = classify_and_reply(email)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
