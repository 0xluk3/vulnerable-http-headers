from flask import Flask

app = Flask(__name__)


@app.route('/guest', methods=['GET', 'POST'])
def hello_world():
    return 'Hello Guest!'

@app.route('/admin', methods=['GET', 'POST'])
def hello_world1():
    return 'Hello Admin!'


if __name__ == '__main__':
    app.run()