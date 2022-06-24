from flask import Flask, request 

app=Flask(__name__)

@app.route("/intro", methods=["GET"])
def intro():
  return "ECSE3038 - Engineering IoT Systems"

@app.route("/name/<name>", methods=["GET"])
def name(name):
  return f"Welcome, {name}, to the IoT class of 2022"

@app.route("/battle", methods=["GET"])
def battle():
    args=request.args
    red=args.get('red')
    blue=args.get('blue')
    return f"{red} could easily beat {blue} in a fight"


if __name__ == '__main__':
    app.run(
       #debug=True,
       port=3000,
       host="0.0.0.0"
    )