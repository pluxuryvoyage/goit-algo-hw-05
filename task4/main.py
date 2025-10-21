def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist. Please check the name."
        except IndexError:
            return "Please provide both name and phone number."
    return inner
            
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Phone number updated"
    else:
        return "Contact not found"

def all_contact(contacts):
    if not contacts:
        return "No contacts saved"
    contact_list = "All contacts:\n"
    for name, phone in contacts.items():
        contact_list += f"{name}: {phone}\n"
    return contact_list.rstrip()

@input_error
def phone(contacts, name):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone: {contacts[name]}"
    else:
        return "Contact not found"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        elif command == "phone":
            print(phone(contacts, args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
