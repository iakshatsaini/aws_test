from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return {"message":"Success", "status":200}

if __name__ == "__main__":
    print("hello dost!!")
    app.run(debug=True)
