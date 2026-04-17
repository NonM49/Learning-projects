from flask import Flask, request, jsonify, flash, render_template
from flask_cors import CORS
import sqlite3
import json
import os
import time

from create_db import get_db

app = Flask(__name__)
CORS(app)


if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        expenses = json.load(f)
else:
    expenses = []

# def save_data():
#     with open("data.json", "w") as f:
#         json.dump(expenses, f, indent = 4) # expenses is the file I want to replace, f is the file object

@app.route("/")
def home():
    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()

    c.execute("SELECT SUM(amount) FROM expenses")
    total = c.fetchone()[0]

    if total is None:
        total = 0

    conn.close()

    expenses = []
    for row in rows:
        expenses.append({
            "id": row[0],
            "name": row[1],
            "amount": row[2]
        })

    return render_template("index.html", expenses=expenses, total=int(total))
    
@app.route("/expenses", methods=["GET"]) #API endpoint
def get_expense():
    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()

    conn.close()

    expenses = []
    for row in rows:
        expenses.append({
            "id": row[0],
            "name": row[1],
            "amount": row[2]
        })

    return expenses


@app.route("/add", methods=["POST"])
def add_expense():

    # receive data from frontend
    data = request.get_json(force = True) #This reads incoming data from user (karg)

    conn = get_db()
    c = conn.cursor()

    c.execute(
        "INSERT INTO expenses (name, amount) VALUES (?, ?)",
        (data["name"], data["amount"])
    )

    conn.commit()
    conn.close()

    return {"message": "added"}

# @app.route("/update/<int:id>", methods=["PUT"])
# def update_expense(id):
#     data = request.get_json()

#     if not data:
#         return jsonify({"error": "No data provided"}), 400

#     if "name" not in data or "amount" not in data:
#         return jsonify({"error": "Missing name or amount"}), 400

#     if not isinstance(data["name"], str):
#         return jsonify({"error": "Name must be a string"}), 400

#     if not isinstance(data["amount"], (int, float)):
#         return jsonify({"error": "Amount must be a number"}), 400
    
#     for expense in expenses:
#         if expense["id"] == id:
#             expense["name"] = data["name"]
#             expense["amount"] = data["amount"]

#             save_data()

#             return jsonify({
#                 "message": "Updated successfully",
#                 "data": expense
#             })
    
#     return jsonify({"error": "Expense not found"}), 404

# @app.route("/delete/<int:id>", methods=["DELETE"])
# def delete_expense(id):

#     for expense in expenses :
#         if expense["id"] == id:
#             expenses.remove(expense)
#             save_data()
#             return jsonify({"message": "Delete successfully"})
        
#     return jsonify({"error": "Expense not found"}), 404

@app.route("/delete", methods=["POST"])
def delete_expense():
    data = request.get_json()
    
    conn = get_db()
    c = conn.cursor()

    c.execute("DELETE FROM expenses WHERE id = ?", (data["id"],))

    conn.commit()
    conn.close()

    return {"message": "deleted"}

@app.route("/update", methods=["POST"])
def update_expense():
    updated_data = request.get_json()

    conn = get_db()
    c = conn.cursor()

    c.execute(
        "UPDATE expenses SET name = ?, amount = ? WHERE id = ?",
        (updated_data["name"], updated_data["amount"], updated_data["id"]) 
    )

    conn.commit()
    conn.close()
    
    return {"message": "updated"}

if __name__ == "__main__":
    app.run(debug = True)