# TODO: Import Contact class
from contact import Contact

class ContactManager():
    def __init__(self):
        # TODO: Create a list to store contacts
        self.contactlist = []
        

    def add_contact(self, contact):
        # TODO: Add contact to the list
        self.contactlist.append(contact)
        

    def list_contacts(self):
        # TODO: Return list of all contacts
        return self.contactlist
        

    def find_contact(self, name):
        # TODO: Return contacts matching search query
        contact_found = []

        for contact in self.contactlist:
            if name.lower() in contact.name.lower():
                contact_found.append(contact.name)
        return contact_found
            
    
    def delete_contact(self, name):
        # TODO: Remove contacts matching the name

        for contact in self.contactlist:
            if name.lower() in contact.name.lower():
                self.contactlist.remove(contact)
                return self.contactlist


    def save_to_file(self, filename):
        # TODO: Write contacts to file

        with open(filename, 'w') as txt_file:
            for contacts in self.contactlist:
                txt_file.write(f"{contacts.name} | Phone: {contacts.phone} | Email: {contacts.email}\n")
        

    def load_from_file(self, filename):
        # TODO: Load contacts from file
        try:
            with open(filename, 'r') as txt_file:
                for current_contact in txt_file:
                    current_contact = current_contact.strip()
                    name, phone, email = current_contact.split('|')

                    if name and phone and email:
                        name_part = name.strip()
                        phone_part = phone.replace("Phone:", "").strip()
                        email_part = email.replace("Email:", "").strip()

                        contact = Contact(name_part, phone_part, email_part)
                        self.contactlist.append(contact)

        except FileNotFoundError:
            print(f'{filename} not found')

        except Exception as e:
            print(f'An error has occured while loading: {e}')
        


