from flask import Flask

import sqlite3
import os
from dotenv import load_dotenv
from route.auth import auth
from route.home import home

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


app.register_blueprint(auth)
app.register_blueprint(home)

if __name__ == "__main__":
    app.run(debug=True)