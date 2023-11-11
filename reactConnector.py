from flask import Flask, request, redirect, url_for, jsonify, Response
from flask_cors import CORS
import json
import placeHolderSql

# import Database

# database = Database.Database()
app = Flask(__name__)
CORS(app)


@app.route("/feed/<username>", methods=["GET", "OPTIONS"])
def returnPeopleAtLocation(username):
    if request.method == "GET":
        # if()
        # val=usersAtLocation(username)
        valDict = placeHolderSql.usersAtLocation(username, "LOC")
        valDict["status"] = 200
        val = json.dumps(valDict)
        return Response(val, status=200)


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
            matchedRow["status"] = 200
            if matchedRow != None:
                return Response(json.dumps(matchedRow), status=200)
    return Response(
        json.dumps({"error": "Incorrect username or password", "status": 201}),
        status=201,
    )


@app.route("/test/<name>")
def returnUsername(name):
    # getname
    # print(request.args.get("n"))
    return name


if __name__ == "__main__":
    app.run()
