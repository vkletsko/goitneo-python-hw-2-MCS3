def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Give me name and phone please."

    return inner


def parse_input(user_input: str) -> (str, list):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        return "invalid_command", []


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added"


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact updated"


@input_error
def show_phone(args: list, contacts: dict) -> str:
    search_name = args[0]
    for name, phone in contacts.items():
        if search_name == name:
            return f"{search_name.title()} {phone}"
        else:
            return f"Contact {search_name.title()} doesn't exist"


def show_all(contacts: dict) -> str:
    phonebook = "Contacts list: \n"
    for name, phone in contacts.items():
        phonebook += "Contact: {} {}\n".format(name.title(), phone)

    return phonebook


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        cmd, *args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, contacts))
        elif cmd == "change":
            print(change_contact(args, contacts))
        elif cmd == "phone":
            print(show_phone(args, contacts))
        elif cmd == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
