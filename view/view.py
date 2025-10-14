import streamlit as st
from controller.controller import add_student, get_all_students, edit_student, remove_student
from bson.objectid import ObjectId

def app():  # wrap all UI code in a function
    st.title("Student Data Entry CRUD Application")

    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    def input_form(data=None):
        if data is None:
            data = {}
        name = st.text_input("Name", value=data.get("Name", ""))
        phone = st.text_input("Phone number", value=data.get("Phone number", ""))
        linkedin = st.text_input("Linkedin", value=data.get("Linkedin", ""))
        email = st.text_input("Email", value=data.get("Email", ""))
        education = st.text_input("Education", value=data.get("Education", ""))
        job = st.text_input("Job", value=data.get("Job", ""))
        location = st.text_input("Location", value=data.get("Location", ""))
        batch = st.text_input("Batch", value=data.get("Batch", ""))
        return {
            "Name": name,
            "Phone number": phone,
            "Linkedin": linkedin,
            "Email": email,
            "Education": education,
            "Job": job,
            "Location": location,
            "Batch": batch
        }

    if choice == "Create":
        st.subheader("Add New Student")
        data = input_form()
        if st.button("Add"):
            if data["Name"].strip() == "":
                st.error("Name cannot be empty!")
            else:
                student_id = add_student(data)
                st.success(f"Student added with ID: {student_id}")

    elif choice == "Read":
        st.subheader("Student List")
        students = get_all_students()
        if students:
            for student in students:
                with st.expander(f"{student['Name']}"):
                    st.write(f"**ID:** {student['_id']}")
                    st.write(f"**Phone:** {student['Phone number']}")
                    st.write(f"**Linkedin:** {student['Linkedin']}")
                    st.write(f"**Email:** {student['Email']}")
                    st.write(f"**Education:** {student['Education']}")
                    st.write(f"**Job:** {student['Job']}")
                    st.write(f"**Location:** {student['Location']}")
                    st.write(f"**Batch:** {student['Batch']}")

    elif choice == "Update":
        st.subheader("Edit Student Data")
        students = get_all_students()
        student_dict = {str(s['_id']): s['Name'] for s in students}
        
        selected_id = st.selectbox("Select Student by ID", list(student_dict.keys()), format_func=lambda x: f"{student_dict[x]} ({x})")
        
        if selected_id:
            selected_student = next((s for s in students if str(s['_id']) == selected_id), None)
            if selected_student:
                updated_data = input_form(selected_student)
                if st.button("Update"):
                    edit_student(ObjectId(selected_id), updated_data)
                    st.success("Student data updated successfully.")

    elif choice == "Delete":
        st.subheader("Delete Student Record")
        students = get_all_students()
        student_dict = {str(s['_id']): s['Name'] for s in students}
        
        selected_id = st.selectbox("Select Student to Delete", list(student_dict.keys()), format_func=lambda x: f"{student_dict[x]} ({x})")
        
        if selected_id:
            selected_student = next((s for s in students if str(s['_id']) == selected_id), None)
            if selected_student:
                st.warning(f"Do you want to delete {selected_student['Name']}?")
                if st.button("Delete"):
                    remove_student(ObjectId(selected_id))
                    st.success("Student deleted successfully.")

