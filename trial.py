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
    "dogsFavoriteActivities": "test",
}
example1 = {
    "username": "test3",
    "phoneNum": "test",
    "city": "test",
    "state":"test",
    "country":"test"
}

database.insertUser(exampleDict)
database.insertUser(example1)

print(database.usersNearby("test"))
