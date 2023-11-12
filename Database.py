from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import gridfs

class Database:
    def __init__(self):
        uri = "mongodb+srv://VAgarwal46:VAgarwal2512@vagarwal46.s1zbw9l.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = client.UserDatabase
        self.db2 = client.trailDatabase
        self.fs = gridfs.GridFS(self.db)
        self.db.users.delete_many({})
        self.db2.trails.delete_many({})

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
            "trail": None,
            "isCurrentlyOnTrail": 0,
            "trailFollowing": None
        }

        self.db.users.insert_one(user)

    def getUser(self, username, password = None):
        user = self.db.users.find_one({"username": username})
        if user == None or (user["password"] != password and password != None):
            return None
        del user["_id"]
        return user
    
    def verify(self, username):
        user = self.getUser(username)
        if user == None:
            return "username Invalid"
        self.db.users.update_one(user, { "$set": { "verification" : 1 } })
        return "Account Verified"

    def updateUser(self, username, updateDict):
        user = self.getUser(username)
        if user == None:
            return "username Invalid"
        self.db.users.update_one(user, {"$set": updateDict})

    def usersNearby(self, username):
        user = self.getUser(username)
        if user == None:
            return "username Invalid"
        users = self.db.users.find({"city": user["city"], "state": user["state"]})
        usersList = list(users)
        for i in usersList:
            del i["_id"]
        return usersList
    
    def setProfilePicture(self, username, profilePicture):
        user = self.getUser(username)
        if user == None:
            return "username Invalid"
        picture = self.fs.put(profilePicture)
        self.updateUser(username, {"profilePicture": picture})

    def getProfilePicture(self, username):
        user = self.getUser(username)
        if user == None:
            return None
        if "profilePicture" in user.keys():
            picture = self.fs.get(user["profilePicture"]).read()
            return picture
        else:
            return None
    
    def setTrail(self, username, trail):
        user = self.getUser(username)
        if user == None:
            return "username Invalid"
        self.updateUser(username, {"trail": trail})
        self.db2.trails.insert_one({"trail": trail, "username": username, "city": user["city"], "likes": 0, "onTrail": 0})

    def getTrail(self, username):
        trail = self.db2.trails.find_one({"username": username})
        if trail == None:
            return None
        del trail["_id"]
        return trail

    def likeTrail(self, username):
        trailToLike = self.db2.trails.find_one({"username": username})
        like = {"$set": {"likes": trailToLike["likes"] + 1 } }
        self.db2.trails.update_one(trailToLike,like)

    def onTrail(self, trailuser, followingUser):
        onTrail = self.db2.trails.find_one({"username": trailuser})
        addOnTrail = {"$set": {"onTrail": onTrail["onTrail"] + 1 } }
        self.db2.trails.update_one(onTrail,addOnTrail)
        user = self.db.users.find_one({"username": followingUser})
        userUpdate = {"$set": {"isCurrentlyOnTrail": 1, "trailFollowing": onTrail["trail"]}}
        self.db.users.update_one(user,userUpdate)
    
    def offTrail(self, trailuser, followingUser):
        user = self.db.users.find_one({"username": followingUser})
        userUpdate = {"$set": {"isCurrentlyOnTrail": 0, "trailFollowing": None}}
        self.db.users.update_one(user,userUpdate)
        offTrail = self.db2.trails.find_one({"username": trailuser})
        addOnTrail = {"$set": {"onTrail": offTrail["onTrail"] - 1 } }
        self.db2.trails.update_one(offTrail,addOnTrail)

    def getPopularTrails(self, city):
        trails = list(self.db2.trails.find({"city": city}))
        maxLikedTrail1 = None
        maxLikedTrail2 = None
        maxLikedTrail3 = None
        popularTrails = []
        if len(trails) >= 3:
            maxLikedTrail1 = trails[0]
            if trails[1]["likes"] > maxLikedTrail1["likes"]:
                maxLikedTrail2 = maxLikedTrail1
                maxLikedTrail1 = trails[1]
            else:
                maxLikedTrail2 = trails[1]
            if trails[2]["likes"] > maxLikedTrail1["likes"]:
                maxLikedTrail3 = maxLikedTrail2
                maxLikedTrail2 = maxLikedTrail1
                maxLikedTrail1 = trails[2]
            elif trails[2]["likes"] > maxLikedTrail2["likes"]:
                maxLikedTrail3 = maxLikedTrail2
                maxLikedTrail2 = trails[2]
            else:
                maxLikedTrail3 = trails[2]
            for i in range(3,len(trails)):
                if trails[i]["likes"] > maxLikedTrail1["likes"]:
                    maxLikedTrail3 = maxLikedTrail2
                    maxLikedTrail2 = maxLikedTrail1
                    maxLikedTrail1 = trails[i]
                elif trails[i]["likes"] > maxLikedTrail2["likes"]:
                    maxLikedTrail3 = maxLikedTrail2
                    maxLikedTrail2 = trails[i]
                elif trails[i]["likes"] > maxLikedTrail3["likes"]:
                    maxLikedTrail3 = trails[i]
            popularTrails = [maxLikedTrail1, maxLikedTrail2, maxLikedTrail3]
        elif len(trails) == 2:
            maxLikedTrail1 = trails[0]
            if trails[1]["likes"] > maxLikedTrail1["likes"]:
                maxLikedTrail2 = maxLikedTrail1
                maxLikedTrail1 = trails[1]
            else:
                maxLikedTrail2 = trails[1]
            popularTrails = [maxLikedTrail1, maxLikedTrail2]
        elif len(trails) == 1:
            popularTrails = [trails[0],]
        else:
            return None
        for i in popularTrails:
            del i["_id"]
        return popularTrails

        