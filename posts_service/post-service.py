from flask import Flask, jsonify

app = Flask(__name__)

posts = [{"id": 1, "title": "Microservices vs Monolith", "user_id": 1}]

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

if __name__ == "__main__":
    app.run(port=5002, debug=True)