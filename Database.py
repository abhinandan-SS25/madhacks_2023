import sqlite3

class Database():
    def __init__(self):
        self.conn = sqlite3.connect(f"myDatabase.sqlite")
        self.cur = self.conn.cursor() 

        # 0:userID, 1:userName, 2:ownerID(foreignKey), 3:dogID(foreignKey), 
        # 4:phoneNum, 5:verification, 6:addressID(foreignKey),
        # 7:password, 8:description
        self.createTable("userInfo", [
            "userID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE",
            "userName TEXT NOT NULL", "ownerID INTEGER", 
            "dogID INTEGER", "phoneNum TEXT UNIQUE", 
            "verification INTEGER NOT NULL", "addressID INTEGER", 
            "password TEXT", "description TEXT"])
        
        # 0:id, 1:name, 2:dob, 3:sex
        self.createTable("ownerInfo", [
            "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE",
            "name TEXT", "dob DATE", "sex TEXT"
        ])

        # 0:id, 1:name, 2:breed, 3:dob,4:sex, 5:favoriteActivities
        self.createTable("dogInfo", [
            "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE",
            "name TEXT", "breed TEXT", "dob DATE", "sex TEXT",
            "favoriteActivities TEXT"
        ])

        # 0:id, 1:streetAddress, 2:city, 3:state, 4:country ,5:pincode
        self.createTable("address", [
             "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE",
             "streetAddress TEXT", "city TEXT", "state TEXT",
             "country TEXT", "pincode TEXT"
        ])

    def createTable(self, name, headersWithProperties):
        query = f'''
        DROP TABLE IF EXISTS {name};
        CREATE TABLE {name} (
        '''
        query += headersWithProperties[0]
        #parsing through the list and creating the query from 
        #creating table with correct columns
        for i in range (1,len(headersWithProperties)):
                query += ","
                query += f"{headersWithProperties[i]}"
        query += ");"
        #executing query
        self.cur.executescript(query)

    def getUser(self, username, password):
        user = dict()
        wherequery = f" where userName = '{username}'"
        if password != None:
            wherequery += f" and password = '{password}'"
        query = "select * from userInfo"
        query += wherequery
        self.cur.execute(query)
        try: extraction = self.cur.fetchall()[0]
        #Try finding better error later
        except IndexError: return None
        user["userName"] = extraction[1]
        user["phoneNum"] = extraction[4]
        user["verification"] = extraction[5]
        user["description"] = extraction[8]
        query = "select addressID,streetAddress,city,state,country,pincode "
        query += "from userInfo,address on userInfo.addressID = address.id "
        query += wherequery
        self.cur.execute(query)
        try: extraction = self.cur.fetchall()[0]
        #Try finding better error later
        except IndexError: return None
        user["streetAddress"] = extraction[1]
        user["city"] = extraction[2]
        user["state"] = extraction[3]
        user["country"] = extraction[4]
        user["pincode"] = extraction[5]
        query = "select ownerID,name,dob,sex "
        query += "from userInfo,ownerInfo on userInfo.ownerID = ownerInfo.id "
        query += wherequery
        self.cur.execute(query)
        try: extraction = self.cur.fetchall()[0]
        #Try finding better error later
        except IndexError: return None
        user["ownerName"] = extraction[1]
        user["ownerDOB"] = extraction[2]
        user["ownerSex"] = extraction[3]
        query = "select dogID,name,breed,dob,sex,favoriteActivities "
        query += "from userInfo,dogInfo on userInfo.dogID = dogInfo.id "
        query += wherequery
        self.cur.execute(query)
        try: extraction = self.cur.fetchall()[0]
        #Try finding better error later
        except IndexError: return None
        user["dogName"] = extraction[1]
        user["dogBreed"] = extraction[2]
        user["dogDOB"] = extraction[3]
        user["dogSex"] = extraction[4]
        user["dogsFavoriteActivities"] = extraction[5]
        return user

    def insertUser(self, userValuesDict):
        userName = userValuesDict["userName"]
        phoneNum = userValuesDict["phoneNum"]
        verification = userValuesDict["verification"]
        password = userValuesDict["password"]
        description = userValuesDict["description"]
        streetAddress = userValuesDict["streetAddress"]
        city = userValuesDict["city"]
        state = userValuesDict["state"]
        country = userValuesDict["country"]
        pincode = userValuesDict["pincode"]
        ownerName = userValuesDict["ownerName"]
        ownerDOB = userValuesDict["ownerDOB"]
        ownerSex = userValuesDict["ownerSex"]
        dogName = userValuesDict["dogName"]
        dogBreed = userValuesDict["dogBreed"]
        dogDOB = userValuesDict["dogDOB"]
        dogSex = userValuesDict["dogSex"]
        dogsFavoriteActivities = userValuesDict["dogsFavoriteActivities"]

        query = "insert into address(streetAddress, city, state, country, pincode)"
        query += f" values ({streetAddress},{city},{state},{country},{pincode})"
        self.cur.executescript(query)
        self.cur.execute(f"select id from address where streetAddress = {streetAddress}" +
                         f" and city = {city} and state  = {state} and country = {country}" +
                         f" and pincode = {pincode}")
        try: addressID = self.cur.fetchall()[0][0]
        except IndexError: return False

        query = "insert into dogInfo(name, breed, dob, sex, favoriteActivities)"
        query += f" values ({dogName}, {dogBreed}, {dogDOB}, {dogSex}, {dogsFavoriteActivities})"
        self.cur.executescript(query)
        self.cur.execute(f"select id from dogInfo where name = {dogName}" +
                         f" and breed = {dogBreed} and dob  = {dogDOB} and sex = {dogSex}" +
                         f" and favoriteActivities = {dogsFavoriteActivities}")
        try: dogID = self.cur.fetchall()[0][0]
        except IndexError: return False

        query = "insert into ownerInfo(name, dob, sex)"
        query += f" values ({ownerName}, {ownerDOB}, {ownerSex})"
        self.cur.executescript(query)
        self.cur.execute(f"select id from ownerInfo where name = {ownerName}" +
                         f" and dob  = {ownerDOB} and sex = {dogSex}")
        try: ownerID = self.cur.fetchall()[0][0]
        except IndexError: return False

        query = "insert into userInfo(userName,ownerID,dogID,phoneNum,verification,addressID,password,description)"
        query += f" values ({userName},{ownerID},{dogID},{phoneNum},{verification},{addressID},{password},{description})"
        self.cur.executescript(query)
        self.cur.execute(f"select id from userInfo where username = {userName}")
        try: ownerID = self.cur.fetchall()[0][0]
        except IndexError: return False
        return True