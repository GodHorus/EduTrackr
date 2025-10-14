from conn.conn import get_db
from bson.objectid import ObjectId

# Initialize database and collection
db = get_db()
collection = db["students"]

# Create
def create_student(data):
    result = collection.insert_one(data)
    return str(result.inserted_id)

# Read
def read_students():
    return list(collection.find())

# Update
def update_student(student_id, data):
    result = collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": data}
    )
    return result.modified_count

# Delete
def delete_student(student_id):
    result = collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count
