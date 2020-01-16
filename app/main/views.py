from flask import Flask
#You need to use following line [app Flask(__name__]
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World with flask"
if __name__ == '__main__':
    app.run(port=5000, debug=True)
