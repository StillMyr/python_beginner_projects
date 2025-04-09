# TODO: Import ContactManager and Contact classes
from contact import Contact
from manager import ContactManager

def main():
    manager = ContactManager()
    manager.load_from_file("contacts.txt")

    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search\n4. Delete\n5. Save & Exit")
        choice = input("Option: ")

        if choice == "1":
            # TODO: Get input and add contact
            #contact = Contact('Karen', '012345', 'karen@gmail.com')
            manager.add_contact(input("Enter name: "),
                                input("Enter phone number: "),
                                input("Enter email: "))

        
        elif choice == "2":
            # TODO: Print all contacts
            contact_list = manager.list_contacts()
            for contact in contact_list:
                print(contact)
                

        elif choice == "3":
            # TODO: Search contacts
            search = manager.find_contact(input("Enter a name: "))
            
            for name in search:
                print(name)
                

        elif choice == "4":
            # TODO: Delete contact
            name = input('Enter a name: ')
            delete = manager.delete_contact(name)

            print(f'{name.capitalize()} has been removed from list')
            print('Updated Contact List: ')

            for name in delete:
                print(name)
                

        elif choice == "5":
            manager.save_to_file("contacts.txt")
            print("Saved. Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
