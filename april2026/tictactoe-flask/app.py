from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = []
next_id = 1

@app.route("/")
def menu():
    return jsonify(expenses)

@app.route("/add", methods=["POST"])
def add_expense():
    global next_id

    data = request.get_json() #This reads incoming data from user

    expense = {
        "id" : next_id,
        "name" : data["name"],
        "amount" : data["amount"]
    }

    expenses.append(expense)
    next_id += 1

    return jsonify({"message" : "Expense added!"})

if __name__ == "__main__":
    app.run(debug = True)