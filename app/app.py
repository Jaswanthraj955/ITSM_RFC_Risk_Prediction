from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():

    return "ITSM ML API Running Successfully"

print("Flask app started")

if __name__ == '__main__':

    print("Starting Flask server")

    app.run(debug=True)