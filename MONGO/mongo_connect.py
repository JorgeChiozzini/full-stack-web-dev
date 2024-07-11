from pymongo import MongoClient
user = ''
password = '' 

#create the connection url
connecturl = "mongodb+srv://{}:{}@cluster0.hr7zdz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(user,password)

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# get database list
print("Getting list of databases")
dbs = connection.list_database_names()

# print the database names

for db in dbs:
    print(db)
print("Closing the connection to the mongodb server")

# close the server connecton
connection.close()