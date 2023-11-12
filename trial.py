from Database import Database

database = Database()
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
    "dogsFavoriteActivities": "test"
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
    "dogsFavoriteActivities": "test2"
}
dict3 = {
    "username": "test3",
    "phoneNum": "test3",
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
    "dogsFavoriteActivities": "test2"
}
dict4 = {
    "username": "test4",
    "phoneNum": "test3",
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
    "dogsFavoriteActivities": "test2"
}
dict5 = {
    "username": "test5",
    "phoneNum": "test3",
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
    "dogsFavoriteActivities": "test2"
}
database.insertUser(exampleDict)
database.insertUser(dict2)
database.insertUser(dict3)
database.insertUser(dict4)
database.insertUser(dict5)
print(database.usersNearby("test"))
#database.setTrail("test", ["list", "of", "trail"])
#database.setTrail("test2", ["list", "of", "trail", "2"])
#database.setTrail("test3", ["list", "of", "trail", "3"])
#database.likeTrail("test")
#database.likeTrail("test")
#database.likeTrail("test")
#database.likeTrail("test2")
#database.likeTrail("test3")
#database.likeTrail("test3")
#database.onTrail("test", "test2")
#print(database.getPopularTrails("test"))
#print(database.getUser("test2"))