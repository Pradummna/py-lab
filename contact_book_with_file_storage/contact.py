# Contact Book System using JSON
import json
import re

file_name = "contact_list.json"

# Check phone no is valid or not
def is_valid_ph_no(ph_no):
    pattern = r'^\d{10}$'
    return re.match(pattern, ph_no) is not None

# Check email is valid or not
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Add contacts
def addContact():
    while True:
        print("Enter contact details.")
        name = input("Name: ").strip()
        
        while not name:
            print("Field cannot be empty. Try Again")
            name = input("Name: ").strip()
    
        while True:
            ph_no = input("Phone number: ").strip()
            
            while not ph_no:
                print("Field cannot be empty. Try Again")
                ph_no = input("Phone number: ").strip()

            if not is_valid_ph_no(ph_no):
                print("Wrong Input. Try Again")
            else:
                break
        
        while True:
            email = input("Email: ").strip()

            while not email:
                print("Field cannot be empty. Try Again")
                email = input("Email: ")

            if not is_valid_email(email):
                print("Wrong Input. Try Again")
            else:
                break
    
        if name and ph_no and email:
            break

    record = {
        'name': name,
        'ph-no': ph_no,
        'email': email
    }
    
    try:
        with open(file_name, 'r') as file:
            contact_lists =  json.load(file)
    
    except (FileNotFoundError, json.JSONDecodeError):
        contact_lists = []

    except Exception as e:
        print(f"An unexpected error occurred: {e}. Run the system again")
        return
    
    contact_lists.append(record)
    with open(file_name, 'w') as file:
        json.dump(contact_lists, file, indent=4)
    print("Saved into file.")
    
# Display contacts record
def displayContact():
    try:
        with open(file_name, 'r') as file:
            records = json.load(file)  # Parse JSON into a Python dictionary
            for record in records:
                print(f"Name: {record['name']}, Ph-No: {record['ph-no']}, Email: {record['email']}")
    except FileNotFoundError:
        print(f"Error: File was not found.")
    except json.JSONDecodeError:
        print("Error: The file is empty or corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Run the system again")

# Search a contact record
def searchContact():
    print("Search a record by name.")
    while True:
        name = input("Name: ").strip()
        if name:
            break
        if not name:
            print("Empty field. Enter name again.")

    try:
        with open(file_name, 'r') as file:
            records =  json.load(file)
            found = False
            for record in records:
                if name == record['name']:
                    found = True
                    print(f"Name: {record['name']}, Ph-No: {record['ph-no']}, Email: {record['email']}")

            if not found:
                print(f"There is no record by Name: {name} in the file.")

    except FileNotFoundError:
        print(f"Error: File was not found.")
    except json.JSONDecodeError:
        print("Error: The file is empty or corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Run the system again")        

# Delete contacts
def deleteContact():
    print("Delete record from file by name.")
    while True:
        name = input("Name: ").strip()
        if name:
            break
        if not name:
            print("Empty field. Enter name again.")

    try:
        with open(file_name, 'r') as file:
            records =  json.load(file)
            found = False
            for record in records:
                if name == record['name']:
                    found = True

            if not found:
                print(f"There is no record by Name: {name} in the file.")

            new_list = []
            for record in records:
                if not name == record['name']:
                    new_list.append(record)
            
            with open(file_name, 'w') as file:
                json.dump(new_list, file, indent=4)

    except FileNotFoundError:
        print(f"Error: File was not found.")
    except json.JSONDecodeError:
        print("Error: The file is empty or corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Run the system again")        

# Update contact details
def updateContact():
    print("Search a record by name to update.")
    while True:
        name = input("Name: ").strip()
        if name:
            break
        if not name:
            print("Empty field. Enter name again.")
    try:
        with open(file_name, 'r') as file:
            contact_lists = json.load(file)
            found = False
            for contact in contact_lists:
                if contact.get("name") == name:
                    found = True
                    print("Contact found! Enter new details (leave blank to keep old):")
                    
                    old_name = contact.get("name", "")
                    old_phone = contact.get("ph-no")
                    old_email = contact.get("email")

                    new_name = input(f"New Name [{old_name}]: ").strip() or old_name

                    while True:
                        new_phone = input(f"Phone number [{old_phone}]: ").strip() or old_phone

                        if not is_valid_ph_no(new_phone):
                            print("Wrong Input. Try Again")
                        else:
                            break
                        
                    while True:
                        new_email = input(f"Email [{old_email}]: ").strip() or old_email

                        if not is_valid_email(new_email):
                            print("Wrong Input. Try Again")
                        else:
                            break
                        
                    contact["name"] = new_name
                    contact["ph-no"] = new_phone
                    contact["email"] = new_email
                    break

            if not found:
                print(f"No contact found with the name {name}.\n")
            else:
                with open(file_name, "w") as file:
                    json.dump(contact_lists, file, indent=4)
                print(f"Contact for {name} updated successfully.\n")
    
    except FileNotFoundError:
        print(f"Error: The file was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file is not a valid JSON file.")
    except IndexError:
        print("Error: The list is empty or the specified index does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# main
while True:
    try:
        print("------ Contact Book System ------")
        print("1. Add Contact.")
        print("2. View All Contacts.")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        print("-------------------------")
        choice = int(input("Enter your choice: "))
    
        if choice == 1:
            addContact()
        elif choice == 2:
            displayContact()
        elif choice == 3:
            searchContact()
        elif choice == 4:
            deleteContact()
        elif choice == 5:
            updateContact()
        elif choice == 6:
            print("Session End. Bye.")
            break
        else:
            print("Wrong Input. Try Again")

    except ValueError:
        print("Invalid input. Please enter a number (1, 2, 3, or 4).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
