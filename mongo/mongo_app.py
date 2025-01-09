# Python with MongoDB
from bson import ObjectId
# Python is a backend technology and it can be connected with different data base applications.
# It can be connected to both SQL and noSQL databases. In this section, we connect Python with
# MongoDB database which is noSQL database.

# MongoDB

# MongoDB is a NoSQL database. MongoDB stores data in a JSON like document which make
# MongoDB very flexible and scalable. Let us see the different terminologies of SQL and
# NoSQL databases. The following table will make the difference between SQL versus NoSQL
# databases.

# from flask import Flask, render_template
# import os, pymongo
#
# MONGO_URI = 'mongodb://root:example@mongodb:27017'
# print(MONGO_URI)
# client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=60000)
# try:
#     print(client.list_database_names())
# except pymongo.errors.ServerSelectionTimeoutError as err:
#     print("Failed to connect to server:", err)
#
# app = Flask(__name__)
#
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)

from flask import Flask
import os
from pymongo import MongoClient


MONGO_URI = 'mongodb://mongoadmin:mongopassword@localhost:27017/'
print("Connecting to MongoDB...")
client = MongoClient(MONGO_URI, directConnection=True)
# print(client.__dict__)

# db = client.thirty_days_of_python
# db.students.insert_one({
#     'name': 'Yosef',
#     'country': 'Germany',
#     'city': 'Frankfurt',
#     'age': 50
# })
#
# names = client.list_database_names()
# print(names)

# students = [
#     {
#         'name': 'Yosef',
#         'country': 'Germany',
#         'city': 'Frankfurt',
#         'age': 50
#     },
#     {
#         'name': 'Peter',
#         'country': 'Germany',
#         'city': 'Darmstadt',
#         'age': 60
#     },
#     {
#         'name': 'Mike',
#         'country': 'Germany',
#         'city': 'Frankfurt',
#         'age': 40
#     }
# ]
#
# for student in students:
#     db.students.insert_one(student)

db = client["thirty_days_of_python"]
# student = db.students.find_one()
# print(student)
#
# student2 = db.students.find_one({'_id': ObjectId('677fd733c5c3221f646a80d4')})
# print(student2)

# students = db.students.find({}, {'_id': 0, 'name': 1, 'country': 1, 'age': 1})
# for stud in students:
#     print(stud)

# query = {
#     'city': 'Darmstadt'
# }
# query = {
#     'age':{'$gt':45}
# }
#
# students = db.students.find(query)
# for stud in students:
#     print(stud)

# students = db.students.find().limit(2)
# for stud in students:
#     print(stud)

# students = db.students.find().sort('name', 1)
# for stud in students:
#     print(stud)
#
# students = db.students.find().sort('name')
# for stud in students:
#     print(stud)
#
# students = db.students.find().sort('name', -1)
# for stud in students:
#     print(stud)

# query = {'age':40}
# new_value = {'$set':{'age':28}}
# db.students.update_one(query, new_value)
# for stud in db.students.find():
#     print(stud)

# query = {'name': 'Mike'}
# db.students.delete_one(query)
# for stud in db.students.find():
#     print(stud)

db.students.drop()

# try:
#     names = client.list_database_names()
#     print("Datenbanken:", names)
# except client.errors.ServerSelectionTimeoutError as err:
#     print("Fehler beim Verbinden mit dem Server:", err)

app = Flask(__name__)

@app.route('/')
def home():
    return "Verbindung zu MongoDB erfolgreich!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)







