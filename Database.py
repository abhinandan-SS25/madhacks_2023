from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Database:
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

    def getUser(self, username, password = None):
        user = self.db.users.find_one({"username": username})
        if user == None or (user["password"] != password and password != None):
            return None
        return user
    
    def verify(self, username):
        self.db.users.update_one({"username": username}, { "$set": { "verification" : 1 } })

    def updateUser(self, username, updateDict):
        user = self.getUser(username)
        self.db.users.update_one(user, {"$set": updateDict})

    def usersNearby(self, username):
        user = self.getUser(username)
        usersNearby = []
        users = self.db.users.find({"city": user["city"], "state": user["state"]})
        usersList = list(users)
        #print(list(users)[1])
        for i in usersList:
            usersNearby.append(i)
        return usersNearby


x = Database()
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
dict2 = {
    "username": "test2",
    "phoneNum": "test2",
    "verification": 1,
    "password": "test2",
    "description": "test2",
    "streetAddress": "test2",
    "city": "test",
    "state": "test",
    "country": "test",
    "pincode": "test",
    "ownerName": "test2",
    "ownerDOB": "test2",
    "ownerSex": "test2",
    "dogName": "test2",
    "dogBreed": "test2",
    "dogDOB": "test2",
    "dogSex": "test2",
    "dogsFavoriteActivities": "test2",
}

x.insertUser(exampleDict)
x.insertUser(dict2)
print(x.usersNearby("test"))