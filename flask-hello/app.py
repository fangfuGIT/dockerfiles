from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "The Flask ,Hello,Docker"
if __name__=='__main__':
    app.run()
