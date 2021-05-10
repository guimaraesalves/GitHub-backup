from flask import Flask

app = Flask("Youtube")

@app.route("/olamundo", methods=["GET"])
def olamundo():
    return{"ola": "mundo"}

app.run()