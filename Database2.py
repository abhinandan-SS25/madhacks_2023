from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

class Database2:
    def __init__(self):
        uri = "mongodb+srv://VAgarwal46:VAgarwal2512@vagarwal46.s1zbw9l.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = client.MyDatabase
        self.db.users.delete_many({})

    def insertUser(self, userValuesDict):
        username = userValuesDict.get("username")
        phoneNum = userValuesDict.get("phoneNum")
        password = userValuesDict.get("password")
        description = userValuesDict.get("description")
        streetAddress = userValuesDict.get("streetAddress")
        city = userValuesDict.get("city")
        state = userValuesDict.get("state")
        country = userValuesDict.get("country")
        pincode = userValuesDict.get("pincode")
        ownerName = userValuesDict.get("ownerName")
        ownerDOB = userValuesDict.get("ownerDOB")
        ownerSex = userValuesDict.get("ownerSex")
        dogName = userValuesDict.get("dogName")
        dogBreed = userValuesDict.get("dogBreed")
        dogDOB = userValuesDict.get("dogDOB")
        dogSex = userValuesDict.get("dogSex")
        dogsFavoriteActivities = userValuesDict.get("dogsFavoriteActivities")

        user = {
            "username": username,
            "verification": 0,
            "phoneNum": phoneNum,
            "password": password,
            "description": description,
            "ownerName": ownerName,
            "ownerDOB": ownerDOB,
            "ownerSex": ownerSex,
            "dogName": dogName,
            "dogBreed": dogBreed,
            "dogDOB": dogDOB,
            "dogSex": dogSex,
            "dogsFavoriteActivities": dogsFavoriteActivities,
            "streetAddress": streetAddress,
            "city": city,
            "state": state,
            "country": country,
            "pincode": pincode
        }

        self.db.users.insert_one(user)

x = Database2()
exampleDict = {
    "username": "test",
    "phoneNum": "test",
    "verification": 0,
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
x.insertUser(exampleDict)
print(x.db.users.count_documents({}))
print(x.db.users.find()[2])