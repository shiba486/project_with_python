# Simple Contact Book using Dictionary

contacts = {}

def show_menu():
    print("\n📱 Contact Book")
    print("1. View all contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

def view_contacts():
    if not contacts:
        print("📭 No contacts saved yet.")
    else:
        print("\n📖 Contact List:")
        for name, number in contacts.items():
            print(f"{name} : {number}")

def add_contact():
    name = input("Enter contact name: ").strip()
    number = input("Enter phone number: ").strip()
    if name in contacts:
        print("⚠️ Contact already exists.")
    else:
        contacts[name] = number
        print("✅ Contact added.")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"🔍 {name} : {contacts[name]}")
    else:
        print("❌ Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        new_number = input("Enter new number: ").strip()
        contacts[name] = new_number
        print("🔁 Contact updated.")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    
    if choice == '1':
        view_contacts()
    elif choice == '2':
        add_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("👋 Exiting Contact Book.")
        break
    else:
        print("❗ Please choose a valid option.")
