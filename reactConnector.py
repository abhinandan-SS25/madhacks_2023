from flask import Flask, request,redirect, url_for, jsonify, Response
from flask_cors import CORS
import json
import placeHolderSql 
app = Flask(__name__)
CORS(app)


@app.route('/login',methods = ['POST','OPTIONS'])
def login():
    #CORS
    if request.method=='OPTIONS':
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res
    
    if request.method == 'POST':
        requestedData=json.loads(request.data)
        inputUsername = requestedData['username']
        inputPassword=requestedData['password']
        matchedRow=placeHolderSql.returnMatchedRow(inputUsername,inputPassword)
        if(matchedRow!=None):
            return jsonify(matchedRow)
    return Response(json.dumps({"error":"Incorrect username or password"}),status=201)

@app.route('/test')
def returnUsername():
    #getname
    return 'NAME'

if __name__ == '__main__':
    app.run()