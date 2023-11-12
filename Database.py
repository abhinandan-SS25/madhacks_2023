from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import gridfs

class Database:
    def __init__(self):
        uri = "mongodb+srv://VAgarwal46:VAgarwal2512@vagarwal46.s1zbw9l.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = client.MyDatabase
        self.fs = gridfs.GridFS(self.db)
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
            "pincode": pincode,
            "profilePicture": profilePicture
        }

        self.db.users.insert_one(user)

    def getUser(self, username, password = None):
        user = self.db.users.find_one({"username": username})
        if user == None or (user["password"] != password and password != None):
            return None
        return user
    
    def verify(self, username):
        if self.usernameFound(username):
            self.db.users.update_one({"username": username}, { "$set": { "verification" : 1 } })
            return "Account Verified"
        return "Invalid username!"

    def updateUser(self, username, updateDict):
        user = self.getUser(username)
        if user == None:
            return "username Invalid"
        self.db.users.update_one(user, {"$set": updateDict})

    def usersNearby(self, username):
        user = self.getUser(username)
        if user == None:
            return "username Invalid"
        usersNearby = []
        users = self.db.users.find({"city": user["city"], "state": user["state"]})
        usersList = list(users)
        #print(list(users)[1])
        for i in usersList:
            usersNearby.append(i)
        return usersNearby
    
    def setProfilePicture(self, username, profilePicture):
        picture = self.fs.put(profilePicture)
        self.updateUser(username, {"profilePicture": picture})

    def usernameFound(self, username):
        user = self.db.users.find_one({"username": username})
        if user == None:
            return False
        return True
        