from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://admin:password@localhost:27017/")

# Create or use an existing database
db_name = "student_data"
db = client[db_name]

# Data templates
student_1 = {'name': 'Ayomide', 'matno': '17cj022483'}
student_2 = {'name': 'Oluwatobi', 'matno': '17cj022484'}

# Create (C)
doc_id_1 = db.students.insert_one(student_1).inserted_id
doc_id_2 = db.students.insert_one(student_2).inserted_id

# Read (R)
retrieved_student_1 = db.students.find_one({'_id': doc_id_1})
print("Retrieved Student 1:", retrieved_student_1)

all_documents = db.students.find()
print("All Documents:")
for doc in all_documents:
    print(doc)

# Update (U)
retrieved_student_2 = db.students.find_one({'_id': doc_id_2})
db.students.update_one({'_id': doc_id_2}, {'$set': {'name': 'Updated Name'}})
updated_student_2 = db.students.find_one({'_id': doc_id_2})
print("Updated Student 2:", updated_student_2)

# Delete (D)
db.students.delete_one({'_id': doc_id_1})
deleted_student_1 = db.students.find_one({'_id': doc_id_1})
if deleted_student_1 is None:
    print("Student 1 deleted successfully")
