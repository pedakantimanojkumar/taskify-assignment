from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///users.db")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)


# Create tables at startup (Flask 3 compatible – no before_first_request)
with app.app_context():
    db.create_all()


@app.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])


@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.json or {}
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()

    return (
        jsonify({"id": user.id, "name": user.name, "email": user.email}),
        201,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
