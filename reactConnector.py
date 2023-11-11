from flask import Flask

app = Flask(__name__)

@app.route('/username')
def returnUsername():
    #getname
    return 'NAME'


if __name__ == '__main__':
    app.run()