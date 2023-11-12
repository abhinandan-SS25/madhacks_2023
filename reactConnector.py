from flask import Flask, request, redirect, url_for, jsonify, Response
from flask_cors import CORS
import json
import placeHolderSql
import Database, re

database = Database.Database()
app = Flask(__name__)
CORS(app)


def createExampleNames():
    exampleDict1 = {
        "username": "arnav",
        "phoneNum": "test",
        "verification": "test",
        "password": "qwerty2@",
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
    exampleDict2 = {
        "username": "vaibhu",
        "phoneNum": "911",
        "password": "qwerty2@",
        "city": "test",
        "state": "test",
        "country": "test",
    }
    exampleDict3 = {
        "username": "nandi",
        "password": "qwerty2@",
        "description": "test",
    }
    exampleDict4 = {
        "username": "bubs",
        "password": "qwerty2@",
        "description": "bubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbubbub",
    }

    database.insertUser(exampleDict1)
    database.insertUser(exampleDict2)
    database.insertUser(exampleDict3)
    database.insertUser(exampleDict4)


createExampleNames()


@app.route("/feed/<username>", methods=["GET", "OPTIONS"])
def returnPeopleAtLocation(username):
    if request.method == "GET":
        # if()
        # val=usersAtLocation(username)
        val = database.usersNearby(username)
        print(val)
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
        inputUsername = str(requestedData["username"]).strip()
        inputPassword = str(requestedData["password"]).strip()
        inputConfirm = str(requestedData["confirm"]).strip()
        if inputUsername == "" or inputPassword == "" or inputConfirm == "":
            return Response(json.dumps({"error": "Invalid Inputs"}), status=202)
        elif len(inputUsername) < 4 or len(inputUsername) > 16:
            return Response(
                json.dumps({"error": "Username must be between 4 to 16 characters"}),
                status=202,
            )
        elif len(inputPassword) < 8 or len(inputPassword) > 16:
            return Response(
                json.dumps({"error": "Password must be between 8 to 16 characters"}),
                status=202,
            )
        elif not re.compile(r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[\W_]).*$").match(
            inputPassword
        ):
            return Response(
                json.dumps(
                    {
                        "error": "Username must be contain atleast 1 alphabet, 1 digit and 1 symbol"
                    }
                ),
                status=202,
            )
        elif inputPassword != inputConfirm:
            return Response(
                json.dumps(
                    {"error": "Please ensure Confirm Password matches Password"}
                ),
                status=202,
            )

        elif database.getUser(inputUsername, None) != None:
            return Response(json.dumps({"error": "User already exists"}), status=203)
        else:
            print(database.getUser(inputUsername, None))
            database.insertUser(requestedData)
            return Response(json.dumps({"error": "SUCCESS"}), status=200)

    return Response(json.dumps({"error": "Neither Post nor Option"}), status=399)


@app.route("/login", methods=["POST", "OPTIONS"])
def login():
    # CORS
    if request.method == "OPTIONS":
        res = Response()
        res.headers["X-Content-Type-Options"] = "*"
        return res

    if request.method == "POST":
        requestedData = json.loads(request.data)
        inputUsername = requestedData["username"].strip()
        inputPassword = requestedData["password"].strip()
        if inputUsername == "" or inputPassword == "":
            return Response(json.dumps({"error": "Invalid Inputs"}), status=202)
        else:
            matchedRow = database.getUser(inputUsername, inputPassword)
        if matchedRow != None:
            return Response(status=200)
    return Response(json.dumps({"error": "Incorrect username or password"}), status=201)


@app.route("/test/<name>")
def returnUsername(name):
    # getname
    # print(request.args.get("n"))
    print(str(database.getUser(name, None)))
    return database.getUser(name, None)


if __name__ == "__main__":
    app.run()
