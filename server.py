import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    global i
    i += 1
    return "Привет от приложения Flask" + str(i)

i = 0
if __name__ == '__main__':

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)