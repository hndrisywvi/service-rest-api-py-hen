from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["GET"]) #standart routing
def login():
    data = request.get_json()
    return jsonify(data)

@app.route("/path-variable/<name>", methods=["GET"]) #path variable
def path_variable(name):
    strWord = f"nama saya: {0}".format(name)
    return jsonify(strWord)

if __name__=="__main__":
    app.run(debug=True)