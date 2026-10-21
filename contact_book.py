# Contact Book
# Collection types: List, Dictionary, and Set

contacts = []
phone_numbers = set()


def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name or not phone or not email:
        print("All fields are required.")
        return

    if phone in phone_numbers:
        print("This phone number already exists.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    phone_numbers.add(phone)

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- CONTACT LIST ---")

    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-" * 25)


def search_contact():
    name = input("Enter name to search: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nContact found!")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return

    print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            phone_numbers.remove(contact["phone"])
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thank you for using the Contact Book!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

