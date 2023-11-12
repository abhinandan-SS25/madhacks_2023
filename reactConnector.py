from flask import Flask, request, redirect, url_for, jsonify, Response
from flask_cors import CORS
import json
import placeHolderSql
import Database

database = Database.Database()
app = Flask(__name__)
CORS(app)

def createExampleNames():
    exampleDict = {
    "userName": "test",
    "phoneNum": "test",
    "verification": "test",
    "password": "test",
    "description": "test",
    "streetAddress": "test",
    "city": "test",
    "state": "test",
    "country": "test",
    "pincode": "test",
    "ownerName": "test",
    "ownerDOB": "test",
    "ownerSex": "test",
    "dogName": "test",
    "dogBreed": "test",
    "dogDOB": "test",
    "dogSex": "test",
    "dogsFavoriteActivities": "test",
}
    database.insertUser(exampleDict)

createExampleNames()    
@app.route("/feed/<username>", methods=["GET", "OPTIONS"])
def returnPeopleAtLocation(username):
    if request.method == "GET":
        # if()
        # val=usersAtLocation(username)
        val = placeHolderSql.usersAtLocation(username, "LOC")
        return jsonify(val)


@app.route("/register", methods=["POST", "OPTIONS"])
def register():
    # CORS
    if request.method == "OPTIONS":
        res = Response()
        res.headers["X-Content-Type-Options"] = "*"
        return res
    if request.method == "POST":
        requestedData = json.loads(request.data)
        inputUsername = requestedData["username"]
        inputPassword = requestedData["password"]
        inputConfirm = requestedData["confirm"]
        database.insertUser(requestedData)
        return Response(json.dumps({"error": "SUCCESS"}), status=200)
        
    return Response(json.dumps({"error": "Incorrect username or password"}), status=201)


@app.route("/login", methods=["POST", "OPTIONS"])
def login():
    # CORS
    if request.method == "OPTIONS":
        res = Response()
        res.headers["X-Content-Type-Options"] = "*"
        return res

    if request.method == "POST":
        requestedData = json.loads(request.data)
        inputUsername = requestedData["username"]
        inputPassword = requestedData["password"]
        if inputPassword != "" and inputPassword != None:
            matchedRow = placeHolderSql.returnMatchedRow(inputUsername, inputPassword)
            if matchedRow != None:
                return jsonify(matchedRow)
    return Response(json.dumps({"error": "Incorrect username or password"}), status=201)


@app.route("/test/<name>")
def returnUsername(name):
    # getname
    # print(request.args.get("n"))
    print(str(database.getUser(name,None)))
    return database.getUser(name,None)


if __name__ == "__main__":
    app.run()
