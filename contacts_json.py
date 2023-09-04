import json

def check_phone_number(number):
    """
    A function to check if the phone number entered is valid
    """
    if number.isdigit():
          #تلفون أرضي
          if len(number)==6:
              return True
          #cellphone number
          if len(number)==9:
              if number[0]=='7':
                  if number[1]=='0' or number[1]=='1' or number[1]=='3' or number[1]=='7' or number[1]=='8':
                      return True
                  else:
                      print("Not a valid cellphone number")
                      return False
              else:
                  print("Not a valid cellphone number")
                  return False
          else:
              print("Not a valid number")
              return False
    else:
            print("Not a number")
            return False

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    verify=check_phone_number(phone)
    if verify:
    
      contacts[name] = {'phone': phone}
      save_contacts(contacts)
      print(f"Contact '{name}' added successfully!")
    else:
        print("You entered a wrong number")
    
    

def update_contact(contacts):
    name = input("Enter the contact's name to update: ")
    new_number = input("Enter the new phone number: ")
    if name in contacts:
        verify=check_phone_number(new_number)
        if verify:
          contacts[name] = {'phone': new_number}
          save_contacts(contacts)
          print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found!")
        
def search_contact(contacts):
    name = input("Enter the contact's name to search: ")
    
    if name in contacts:
        contact_info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact_info['phone']}")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact(contacts):
    name = input("Enter the contact's name to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def display_all_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
    
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contacts Program ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            display_all_contacts(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()