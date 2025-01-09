
from flask import Flask,  Response, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime
import json
import os

app = Flask(__name__)


MONGO_URI = 'mongodb://admin:admin@localhost:27017/'
print("Connecting to MongoDB...")
client = MongoClient(MONGO_URI, directConnection=True)

db = client['thirty_days_of_python']

student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]

students = db.students
if  students.count_documents({}) <= 0:
    for student in student_list:
        db.students.insert_one(student)


@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    studs = db.students.find()
    return Response(dumps(studs), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student(id):
    studs = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(studs), mimetype='application/json')

@app.route('/api/v1.0/students', methods = ['POST'])
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }
    db.students.insert_one(student)
    return Response(dumps(student), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods = ['PUT'])
def update_student(id):
    query = {'_id': ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }
    db.students.update_one(student)
    return Response(dumps(student), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.students.delete_one({"_id":ObjectId(id)})
    return Response(dumps(id), mimetype='application/json')

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
