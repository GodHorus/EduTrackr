from service.service import create_student, read_students, update_student, delete_student

def add_student(data):
    return create_student(data)

def get_all_students():
    return read_students()

def edit_student(student_id, data):
    return update_student(student_id, data)

def remove_student(student_id):
    return delete_student(student_id)
