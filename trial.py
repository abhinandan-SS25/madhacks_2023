from Database import Database

database = Database()
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
example1 = {
    "userName": "test",
    "phoneNum": "test",
}

database.insertUser(example1)
print(database.getUser("test","test"))
