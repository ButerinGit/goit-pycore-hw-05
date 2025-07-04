def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "User not found, please enter a valid user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args.strip()
    return f"{name}: {contacts[name]}"

@input_error
def show_all(_):
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

# Приклад простого циклу бота
while True:
    command = input("Enter a command: ").lower()
    if command == "exit":
        break
    elif command.startswith("add"):
        args = command[3:].strip()
        print(add_contact(args))
    elif command.startswith("phone"):
        args = command[5:].strip()
        print(get_phone(args))
    elif command == "all":
        print(show_all(""))
    else:
        print("Unknown command.")
