from flask import Flask, request,redirect, url_for, jsonify, Response
from flask_cors import CORS
import json
import placeHolderSql 
app = Flask(__name__)
CORS(app)


@app.route('/login',methods = ['POST','OPTIONS'])
def login():
    if request.method=='OPTIONS':
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res
    print("Called")
    if request.method == 'POST':
        print("S1")
        requestedData=json.loads(request.data)
        inputUsername = requestedData['username']
        userInList=placeHolderSql.isUserInListMethod(inputUsername)
        print(userInList)
        if(userInList):
            inputPassword=requestedData['password']
            #correctPassword=isCorrectMethod(inputUsername)
            correctPassword=True
            print(inputUsername)
            val=placeHolderSql.getRow(inputUsername)
            if(correctPassword):
                return jsonify(val)
    return Response(json.dumps({"error":"DANCEDANCEBABY"}),status=201)

@app.route('/test')
def returnUsername():
    #getname
    return 'NAME'

if __name__ == '__main__':
    app.run()