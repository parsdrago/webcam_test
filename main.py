from flask import Flask

app = Flask(__name__, static_folder='static')

app.run('0.0.0.0')