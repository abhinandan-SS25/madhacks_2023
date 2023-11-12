from flask import Flask, request, redirect, url_for, jsonify, Response
from flask_cors import CORS
import json, placeHolderSql, Database, re, datetime

database = Database.Database()
app = Flask(__name__)
CORS(app)

def defaultValues():
    defaultDict = {
        "username": "root",
        "password": "root",
    }
    
    database.insertUser(defaultDict)

    database.setTrail(
        "root",
        {
            "coordinates": [
                [0, 0],
                [0, 0],
            ],
            "type": "Polygon",
        },
        {"lat": "0", "lon": "0"},
    )



def createExampleNames():
    exampleDict1 = {
        "city": "Madison",
        "country": "USA",
        "description": "A little lazy, but likes going on walks.",
        "dogBreed": "Golden Retriever",
        "dogDOB": "11-10-2017",
        "dogName": "Sparks",
        "dogSex": "M",
        "dogsFavoriteActivities": "Sleeping",
        "isCurrentlyOnTrail": 0,
        "ownerDOB": "11-10-2003",
        "ownerName": "John",
        "ownerSex": "M",
        "password": "rootjohn2@",
        "phoneNum": "6081232291",
        "pincode": "12312",
        "state": "WI",
        "streetAddress": "123 W Park St",
        "username": "john",
        "verification": 0,
    }
    exampleDict2 = {
        "city": "Madison",
        "country": "USA",
        "description": "An excited ball of energy.",
        "dogBreed": "Poodle",
        "dogDOB": "01-10-2011",
        "dogName": "Daisy",
        "dogSex": "F",
        "dogsFavoriteActivities": "Running",
        "isCurrentlyOnTrail": 0,
        "ownerDOB": "11-02-2003",
        "ownerName": "May",
        "ownerSex": "F",
        "password": "rootmay2@",
        "phoneNum": "6082222291",
        "pincode": "12312",
        "state": "WI",
        "streetAddress": "323 W Park St",
        "username": "may12",
        "verification": 0,
    }
    exampleDict3 = {
        "city": "Madison",
        "country": "USA",
        "description": "An excited ball of energy.",
        "dogBreed": "Chihuahua",
        "dogDOB": "01-10-2017",
        "dogName": "Sunny",
        "dogSex": "M",
        "dogsFavoriteActivities": "Eating",
        "isCurrentlyOnTrail": 0,
        "ownerDOB": "11-02-2003",
        "ownerName": "Mathew",
        "ownerSex": "M",
        "password": "rootmatt2@",
        "phoneNum": "6081111291",
        "pincode": "12312",
        "state": "WI",
        "streetAddress": "223 W Park St",
        "username": "matt",
        "verification": 0,
    }
    
    database.insertUser(exampleDict1)
    database.insertUser(exampleDict2)
    database.insertUser(exampleDict3)

    database.setTrail(
        "john",
        {
            "coordinates": [
                [88.40329706668854, 22.49435178996269],
                [88.40484738349915, 22.494153713312638],
            ],
            "type": "Polygon",
        },
        {"lat": "43.2573529", "lon": "-79.8675813"},
    )
    database.setTrail(
        "may12",
        {
            "coordinates": [
                [78.40329706668854, 22.49435178996269],
                [78.40484738349915, 22.494153713312638],
            ],
            "type": "Polygon",
        },
        {"lat": "43.2573529", "lon": "-79.8675813"},
    )
    database.setTrail(
        "matt",
        {
            "coordinates": [
                [68.40329706668854, 22.49435178996269],
                [68.40484738349915, 22.494153713312638],
            ],
            "type": "Polygon",
        },
        {"lat": "43.2573529", "lon": "-79.8675813"},
    )

defaultValues()

createExampleNames()

@app.route("/routes/like",methods=["POST","GET","OPTIONS"])
def like():
    # CORS
    if request.method == "OPTIONS":
        res = Response()
        res.headers["X-Content-Type-Options"] = "*"
        return res
    if request.method == "POST":
        requestedData = json.loads(request.data)
        username=requestedData["username"]
        database.likeTrail(username)
        returnedTrail=database.getTrail(username)
        return Response(json.dumps(returnedTrail), status=200)


@app.route("/save_shapes", methods=["POST", "OPTIONS"])
def save_shapes():
    # CORS
    if request.method == "OPTIONS":
        res = Response()
        res.headers["X-Content-Type-Options"] = "*"
        return res
    if request.method == "POST":
        requestedData = json.loads(request.data)
        database.setTrail(
            requestedData["username"].strip(),
            requestedData["data"][0],
            requestedData["center"],
        )
        return Response(json.dumps({"status": 200}), status=200)


@app.route("/trails/<username>", methods=["GET", "OPTIONS"])
def returnSingleTrail(username):
    # CORS
    if request.method == "OPTIONS":
        res = Response()
        res.headers["X-Content-Type-Options"] = "*"
        return res
    if request.method == "GET":
        returnedTrail=database.getTrail(username)
        return Response(json.dumps(returnedTrail), status=200)


@app.route("/feed/<username>", methods=["GET", "OPTIONS"])
def returnPeopleAtLocation(username):
    # CORS
    if request.method == "OPTIONS":
        res = Response()
        res.headers["X-Content-Type-Options"] = "*"
        return res
    if request.method == "GET":
        val = {}
        tempVal = database.usersNearby(username)
        val["data"] = tempVal
        val["status"] = 200
        val["trails"] = database.getPopularTrails(val["data"][0]["city"])
        #print(val)
        return Response(json.dumps(val), status=200)


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
            database.insertUser(requestedData)
            requestedData["status"] = 200
            return Response(json.dumps(requestedData), status=200)

    return Response(json.dumps({"error": "Neither Post nor Option"}), status=399)


@app.route("/update", methods=["POST", "OPTIONS"])
def update():
    # CORS
    if request.method == "OPTIONS":
        res = Response()
        res.headers["X-Content-Type-Options"] = "*"
        return res
    if request.method == "POST":
        requestedData = dict(json.loads(request.data))
        if database.getUser(requestedData["username"].strip()) == None:
            return Response(json.dumps({"error": "User not found"}), status=201)

        # ownerName
        if len(requestedData["ownerName"].strip()) > 0:
            if len(requestedData["ownerName"].strip()) > 50:
                return Response(
                    json.dumps({"error": "Owner name must be less than 50 characters"}),
                    status=202,
                )
            elif not str(requestedData["ownerName"].strip()).replace(" ", "").isalpha():
                return Response(
                    json.dumps({"error": "Owner name must be be alphabetical"}),
                    status=202,
                )
        # ownerDOB
        if len(requestedData["ownerDOB"].strip()) > 0:
            try:
                month, day, year = str(requestedData["ownerDOB"]).strip().split("-")
                if not (day.isdigit() and month.isdigit() and year.isdigit()):
                    return Response(
                        json.dumps(
                            {"error": "Owner's DOB must be in mm-dd-yyyy order"}
                        ),
                        status=202,
                    )
                month, day, year = int(month), int(day), int(year)
                if (
                    (day < 1 or month < 1 or year < 1)
                    or (month > 12 or year > datetime.date.today().year)
                    or ((day == 28 or day == 29) and month != 2)
                    or (day > 30 and month not in [1, 3, 5, 7, 8, 10, 12])
                ):
                    return Response(
                        json.dumps({"error": "Owner's DOB is invalid"}),
                        status=202,
                    )
            except ValueError:
                return Response(
                    json.dumps({"error": "Owner's DOB must be in mm-dd-yyyy order"}),
                    status=202,
                )
        # phoneNum

        if len(requestedData["phoneNum"].strip()) > 0:
            if len(requestedData["phoneNum"].strip()) != 10:
                return Response(
                    json.dumps({"error": "Phone number must be 10 digits"}),
                    status=202,
                )
            elif not (str(requestedData["phoneNum"].strip()).isdigit()):
                return Response(
                    json.dumps({"error": "Phone number must be in digits"}),
                    status=202,
                )

        # ownerSex

        if len(requestedData["ownerSex"].strip()) > 0:
            if str(requestedData["ownerSex"]).strip().lower() not in ["f", "m", "x"]:
                return Response(
                    json.dumps({"error": "Please select fromm f, m, x"}),
                    status=202,
                )

        # description

        if len(requestedData["description"].strip()) > 0:
            if len(requestedData["description"]) > 501:
                return Response(
                    json.dumps(
                        {
                            "error": "Please enter description between 1 to 500 characters"
                        }
                    ),
                    status=202,
                )

        # dogName
        if len(requestedData["dogName"].strip()) > 0:
            if len(requestedData["dogName"].strip()) > 50:
                return Response(
                    json.dumps({"error": "Dog name must be less than 50 characters"}),
                    status=202,
                )
            elif not str(requestedData["dogName"].strip()).replace(" ", "").isalpha():
                return Response(
                    json.dumps({"error": "Dog name must be be alphabetical"}),
                    status=202,
                )
        # streetAddress

        if len(requestedData["streetAddress"].strip()) > 0:
            if len(requestedData["streetAddress"]) > 501:
                return Response(
                    json.dumps(
                        {
                            "error": "Please enter street address between 1 to 500 characters"
                        }
                    ),
                    status=202,
                )
        # dogBreed
        if len(requestedData["dogBreed"].strip()) > 0:
            if len(requestedData["dogBreed"].strip()) > 50:
                return Response(
                    json.dumps({"error": "Dog breed must be less than 50 characters"}),
                    status=202,
                )
            elif not str(requestedData["dogBreed"].strip()).replace(" ", "").isalpha():
                return Response(
                    json.dumps({"error": "Dog breed must be be alphabetical"}),
                    status=202,
                )
        # city
        if len(requestedData["city"].strip()) > 0:
            if len(requestedData["city"].strip()) > 50:
                return Response(
                    json.dumps({"error": "City name must be less than 50 characters"}),
                    status=202,
                )
            elif not str(requestedData["city"].strip()).replace(" ", "").isalpha():
                return Response(
                    json.dumps({"error": "City name must be be alphabetical"}),
                    status=202,
                )
        # dogDOB
        if len(requestedData["dogDOB"].strip()) > 0:
            try:
                month, day, year = str(requestedData["dogDOB"]).strip().split("-")
                if not (day.isdigit() and month.isdigit() and year.isdigit()):
                    return Response(
                        json.dumps({"error": "Dog's DOB must be in mm-dd-yyyy order"}),
                        status=202,
                    )
                month, day, year = int(month), int(day), int(year)
                if (
                    (day < 1 or month < 1 or year < 1)
                    or (month > 12 or year > datetime.date.today().year)
                    or ((day == 28 or day == 29) and month != 2)
                    or (day > 30 and month not in [1, 3, 5, 7, 8, 10, 12])
                ):
                    return Response(
                        json.dumps({"error": "Dog's DOB is invalid"}),
                        status=202,
                    )
            except ValueError:
                return Response(
                    json.dumps({"error": "Dog's DOB must be in mm-dd-yyyy order"}),
                    status=202,
                )
        # state
        if len(requestedData["state"].strip()) > 0:
            if len(requestedData["state"].strip()) > 50:
                return Response(
                    json.dumps({"error": "State name must be less than 50 characters"}),
                    status=202,
                )
            elif not str(requestedData["state"].strip()).replace(" ", "").isalpha():
                return Response(
                    json.dumps({"error": "State name must be be alphabetical"}),
                    status=202,
                )
        # dogSex

        if len(requestedData["dogSex"].strip()) > 0:
            if str(requestedData["dogSex"]).strip().lower() not in ["f", "m", "x"]:
                return Response(
                    json.dumps({"error": "Please select fromm f, m, x"}),
                    status=202,
                )
        # country
        if len(requestedData["country"].strip()) > 0:
            if len(requestedData["country"].strip()) > 50:
                return Response(
                    json.dumps(
                        {"error": "Country name must be less than 50 characters"}
                    ),
                    status=202,
                )
            elif not str(requestedData["country"].strip()).replace(" ", "").isalpha():
                return Response(
                    json.dumps({"error": "Country name must be be alphabetical"}),
                    status=202,
                )
        # dogsFavoriteActivities

        if len(requestedData["dogsFavoriteActivities"].strip()) > 0:
            if len(requestedData["dogsFavoriteActivities"]) > 501:
                return Response(
                    json.dumps(
                        {
                            "error": "Please enter dogs favorite activities between 1 to 500 characters"
                        }
                    ),
                    status=202,
                )
        # pincode

        if len(requestedData["pincode"].strip()) > 0:
            if len(requestedData["pincode"].strip()) != 5:
                return Response(
                    json.dumps({"error": "Pincode must be 5 digits"}),
                    status=202,
                )
            elif not (str(requestedData["pincode"].strip()).isdigit()):
                return Response(
                    json.dumps({"error": "Pincode must be in digits"}),
                    status=202,
                )

        database.updateUser(requestedData["username"].strip(), requestedData)
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
            matchedRow["status"] = 200
            return Response(json.dumps(matchedRow), status=200)
    return Response(json.dumps({"error": "Incorrect username or password"}), status=201)


@app.route("/test/<name>")
def returnUsername(name):
    # getname
    # print(request.args.get("n"))
    print(str(database.getUser(name, None)))
    return database.getUser(name, None)


if __name__ == "__main__":
    app.run()
