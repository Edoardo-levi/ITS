from flask import *

app= Flask(__name__)

@app.route('/')
def home() ->str:
    return f"<p> Questo è un esempio di Flask</p>"


if __name__ == "__main__":
    app.run(debug=True)