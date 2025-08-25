# Contact Book with Add, View, Delete, and Update
FILE_NAME = "contacts.txt"

# ADD CONTACT
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"Name: {name}, Phone: {phone}, Email: {email}\n")
    print(f"Contact for {name} added successfully.\n")

# VIEW CONTACTS
def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if contacts:
                print("\n--- Contact List ---")
                for contact in contacts:
                    print(contact.strip())
                print()
            else:
                print("No contacts found.\n")
    except FileNotFoundError:
        print("No contact file found. Add some contacts first.\n")

# DELETE CONTACT
def delete_contact():
    name = input("Enter Name to Delete: ").strip()
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        updated_contacts = [contact for contact in contacts if not contact.startswith(f"Name: {name},")]

        if len(updated_contacts) == len(contacts):
            print(f"No contact found with the name {name}.\n")
        else:
            with open(FILE_NAME, "w") as file:
                file.writelines(updated_contacts)
            print(f"Contact for {name} deleted successfully.\n")
    except FileNotFoundError:
        print("No contact file found.\n")

# UPDATE CONTACT
def update_contact():
    name = input("Enter Name to Update: ").strip()
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()

        found = False
        for i in range(len(contacts)):
            if contacts[i].startswith(f"Name: {name},"):
                found = True
                print("Contact found! Enter new details (leave blank to keep old):")
                
                # Extract old details
                parts = contacts[i].strip().split(", ")
                old_phone = parts[1].replace("Phone: ", "")
                old_email = parts[2].replace("Email: ", "")

                # Get new details
                new_phone = input(f"New Phone [{old_phone}]: ").strip() or old_phone
                new_email = input(f"New Email [{old_email}]: ").strip() or old_email

                contacts[i] = f"Name: {name}, Phone: {new_phone}, Email: {new_email}\n"
                break

        if not found:
            print(f"No contact found with the name {name}.\n")
        else:
            with open(FILE_NAME, "w") as file:
                file.writelines(contacts)
            print(f"Contact for {name} updated successfully.\n")
    except FileNotFoundError:
        print("No contact file found.\n")

# MAIN MENU
while True:
    print("===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
