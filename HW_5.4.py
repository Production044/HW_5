def parse_input(user_input):
    cmd, *args = user_input.split(maxsplit=2)
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid number of arguments for the command."

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
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phone(args, contacts):
    name, *_ = args
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


@input_error
def show_all(contacts):
    if contacts:
        return '\n'.join([f"{name}: {phone_number}" for name, phone_number in contacts.items()])
    else:
        return "No contacts saved."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError as e:
                print(e)

        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError as e:
                print(e)

        elif command == "phone":
            try:
                print(show_phone(args, contacts))
            except ValueError as e:
                print(e)

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
