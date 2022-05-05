from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def hello_world():
    username = request.args.get('username')
    password = request.args.get('password')
    print(username)
    return "nveen"


if __name__ == '__main__':
    app.run()