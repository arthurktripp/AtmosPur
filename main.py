from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  title = "AtmosPür"
  return render_template('index.html',
                        title = title)




if __name__ == "__main__":
  app.run(port=5001, debug = True)
