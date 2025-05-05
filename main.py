import json
import os

class ContactBook:
    def __init__(self):
        self.contacts_file = "contacts.json"
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.contacts_file):
            with open(self.contacts_file, 'r') as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open(self.contacts_file, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
            return
        for i, contact in enumerate(self.contacts, 1):
            print(f"\nContact #{i}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")

    def update_contact(self, index, name, phone, email):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = {
                "name": name,
                "phone": phone,
                "email": email
            }
            self.save_contacts()
            print(f"Contact updated successfully!")
        else:
            print("Invalid contact index!")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted = self.contacts.pop(index)
            self.save_contacts()
            print(f"Contact {deleted['name']} deleted successfully!")
        else:
            print("Invalid contact index!")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        
        elif choice == "2":
            contact_book.view_contacts()
        
        elif choice == "3":
            contact_book.view_contacts()
            index = int(input("Enter contact number to update: ")) - 1
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contact_book.update_contact(index, name, phone, email)
        
        elif choice == "4":
            contact_book.view_contacts()
            index = int(input("Enter contact number to delete: ")) - 1
            contact_book.delete_contact(index)
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()