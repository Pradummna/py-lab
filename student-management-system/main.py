from services.manager import StudentManager

# Input warning empty field
def input_warning():
    print("\nEmpty Field. Fill the correct details\n")

def print_value_error():
    print("Invalid input. Enter a number.")

# Take students input values
def addStudent(sm):
    print("Enter student details.")
    while True:
        try:
            roll = int(input("Roll: "))
            if roll <= 0:
                input_warning()
                continue
            break
        except ValueError:
            print_value_error()

    while True:
        name = input("Name: ").strip()
        if not name:
            input_warning()
            continue
        break
    
    marks = {}
    while True:
        try:
            total_subject = int(input("Enter total number of subjects: "))
            if total_subject <= 0:
                input_warning()
                continue
            break
        except ValueError:
            print_value_error()

    for i in range(total_subject):
        while True:
            subject = input("Subject name: ").strip()
            if not subject:
                input_warning()
                continue
            try:
                sub_marks = int(input("Marks: ").strip())
            except ValueError:
                print_value_error()
                continue
            marks[subject] = sub_marks
            break
    
    sm.add_student(roll, name, marks)

# Take updated values
def updateStudent(sm):
    while True:
        try:
            roll = int(input("Enter Roll No to update: "))
            if roll > 0:
                break
            input_warning()
        except ValueError:
            print_value_error()

    exist_roll = sm.get_student(roll)
    if not exist_roll:
        print(f"No student record found by Roll: {roll}.")
        return
    
    name = input("Enter new name (leave blank to keep old name): ").strip()
    
    while True:
        update_marks = input("Do you want to update marks? (y/n): ").strip().lower()
        if update_marks in ("y", "n"):
            break
        print("Please enter 'y' or 'n'.")
        
    marks = None
    if update_marks == 'y':
        marks = {}
        while True:
            try:
                total_subject = int(input("Enter total number of subjects: "))
                if total_subject > 0:
                    break
                input_warning()
            except ValueError:
                print_value_error()
            
        for i in range(total_subject):
            while True:
                subject = input("Subject name: ").strip()
                if not subject:
                    input_warning()
                    continue
                try:
                    sub_marks = int(input("Marks: ").strip())
                except ValueError:
                    print_value_error()
                    continue
                marks[subject] = sub_marks
                break

    sm.update_student(roll, name if name else None, marks)

def main():
    sm = StudentManager()
    while True:
        print("\n------ Student Record Management System ------")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        print("---------------------------------------------")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print_value_error()
            continue
    
        if choice == 1:
            addStudent(sm)

        elif choice == 2:
            sm.view_students()

        elif choice == 3:
            while True:
                try:
                    roll = int(input("Enter roll no: "))
                    if roll > 0:
                        sm.search_student(roll)
                        break
                except ValueError:
                    print_value_error()

        elif choice == 4:
            while True:
                try:
                    roll = int(input("Enter roll no: "))
                    if roll > 0:
                        sm.delete_student(roll)   # ✅ fixed
                        break
                except ValueError:
                    print_value_error()

        elif choice == 5:
            updateStudent(sm)

        elif choice == 6:
            print("Session End. Bye.")
            break
        
        else:
            print("Wrong Input. Try Again")

if __name__ == "__main__":
    main()
