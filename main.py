'''
Schema:-


BookMaker => {
    "id" : integer,
    "name" : string,
    "isActive" : boolean
}


Event => {
    "id" : integer,
    "name" : string,
    "isActive" : boolean,
    .   .       .       .
    .   .       .       .
    .   .       .       .
    "__"  : "---"
}


Pros:- 
    1. instead of regular loops, used list compression 
    2. instead of inserting one by one, used the powerful method insert many 
    3. In this case, we are transferring event details to multiple bookmakers so that the bookmaker can easily know event details from the transferred data. 

Cons:- 
    1. Time complexity is n*m ( where m is number of events and n is number of bookmaker)
    2. Iterations makes code runtime slower
    

'''


# Implementation ...!
from pymongo import MongoClient  # let's import mongoclient

client = MongoClient("https://admin:admin_password@localhost:27017") # MongoDB client 

events, bookmakers = client.events.events, client.bookmakers.bookmaker # let's get data collectoins !


client.oddsandmore.maps.insert_many( # insert mapped data into database .. !
    [
        event.update(
            {
                "bookmakerId"  : bookmaker.id,
                "bookmakerName" : bookmaker.name
            } # let's update event with bookmaker detials 
        )
        for event in events.find("{}") # lets fetch all events ... 
        for bookmaker in bookmakers.find({'isActive' : True}) # lets fetch bookmakers and filter it 
        
    ]
    
)






