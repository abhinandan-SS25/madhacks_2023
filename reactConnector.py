from flask import Flask, request,redirect, url_for, jsonify
import placeHolderSql 
app = Flask(__name__)


@app.route('/login',methods = ['POST'])
def login():
    if request.method == 'POST':
        inputUsername = request.form['username']
        userInList=placeHolderSql.isUserInListMethod(inputUsername)
        if(userInList):
            inputPassword=request.form['password']
            #correctPassword=isCorrectMethod(inputUsername)
            correctPassword=True
            val=placeHolderSql.getRow(inputUsername)
            if(correctPassword):
                return val
    return None

@app.route('/test')
def returnUsername():
    #getname
    return 'NAME'

if __name__ == '__main__':
    app.run()