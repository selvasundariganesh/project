class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

    def update_contact(self, name, phone=None, email=None):
        contact = self.search_contact(name)
        if contact:
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            return True
        return False


manager = ContactManager()
manager.add_contact(Contact("SELVA SUNDARI", "987-654-3210", "SELLU@example.com"))
manager.add_contact(Contact("HARINI GANESH", "987-654-3210", "HARINI@example.com"))

print("All contacts:")
manager.display_contacts()

print("\nSearch for John Doe:")
print(manager.search_contact("HARINI GANESH"))

print("\nUpdate HARINI GANESH phone number:")
manager.update_contact("HARINI GANESH", phone="555-555-5555")
manager.display_contacts()

print("\nRemove HARINI GANESH:")
manager.remove_contact("HARINI GANESH")
manager.display_contacts()
