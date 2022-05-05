import pymongo


def main():
    
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017", username="admin", password="admin")

    collection1 = mongoClient.db1.activeEvents
    map = mongoClient.oddsandmore.mapping

    for d in collection1.find({"bookmakerId" : 12 , "bookmakerName" : "goldbet" }) : map.insert_one(d)


main()
