import json
import os
from models.student import Student

class StudentManager:
    def __init__(self, file_name = "student.json"):
        self.file_name = file_name
        self.students = []
        self.load_data()

    # Load json file
    def load_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, "r") as file:
                    data = json.load(file)
                    self.students = [Student.from_dict(student) for student in data]
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error in loading data: {e}. Resetting file.")
                self.students = []
                self.save_data()
        else:
            self.students = []

    # save (new or update) data to json file
    def save_data(self):
        with open(self.file_name, "w") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    # search student record is exist or not for (Searching and Update student record)
    def get_student(self, roll):
        for student in self.students:
            if student.roll == roll:
                return student # return student obj if found
        return None

    # add new student record
    def add_student(self, roll, name, marks):
        if any(student.roll == roll for student in self.students):
            print("Given roll no is already exist. Try different one.")
            return False
        
        self.students.append(Student(roll, name, marks))
        self.save_data()
        print("Student record successfully added.")
        return True

    # view existing students record from file
    def view_students(self):
        if not self.students:
            print("No students record in file.")
            return
        print("Display All Students Record")
        for index, student in enumerate(self.students, start=1):
            print(f"SL No: {index} | Roll: {student.roll} | Name: {student.name} | Marks: {student.marks}")

    # search a student record from file
    def search_student(self, roll):
        student = self.get_student(roll)
        if student:
            print(f"Found: Roll: {student.roll} | Name: {student.name} | Marks: {student.marks}")
            return student
        print(f"No student record found by Roll: {roll}.")
        return None
        
    # update existing students record
    def update_student(self, roll, name=None, marks=None):
        student = self.get_student(roll)
        if not student:
            print(f"No student record found by Roll: {roll}.")            
            return False
        
        if name:
            student.name = name
        if marks:
            student.marks = marks
        self.save_data()
        print("Record updated successfully")
        return True

    # delete students record
    def delete_student(self, roll):
        for student in self.students:
            if student.roll == roll:
                self.students.remove(student)
                self.save_data()
                print("Student record successfully deleted.")
                return True
        print(f"No student record found by Roll: {roll}.")
        return False
