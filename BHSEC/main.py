from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def files():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, port=6969)