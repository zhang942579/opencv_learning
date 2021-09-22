from flask import Flask

add = Flask(__name__)

@add.route('/index')
def index():
    return 'Hello world'


if __name__ == '__main__':
    add.run()

