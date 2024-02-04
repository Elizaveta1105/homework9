from types import FunctionType

CONTACTS = {}

help = '''
You can use these commands
hello
add <name> <phone>
change <name> <phone>
phone <name>
show all
close
exit'''


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except IndexError:
            return help
        except KeyError:
            return help
        except ValueError as error:
            return "Input the name"
        except TypeError:
            return help

    return inner


@input_error
def hello(customer_input):
    return "How can I help you?"


@input_error
def add(customer_input):
    action, name, phone = customer_input.split()
    if name not in CONTACTS:
        CONTACTS[name] = phone
        return "Contact added successfully!"
    raise TypeError("Contact already exists")


@input_error
def change(customer_input):
    action, name, phone = customer_input.split()
    if name in CONTACTS:
        CONTACTS[name] = phone
        return "Contact updated successfully!"
    raise TypeError("Contact already exists")


@input_error
def get_phone(customer_input):
    action, name = customer_input.split()
    try:
        result = CONTACTS[name]
    except:
        raise TypeError("Contact not found")

    return f'{name}: {result}'


@input_error
def show_all(customer_input):
    if customer_input != "show all":
        raise KeyError

    if len(CONTACTS) == 0:
        return "Contacts library is empty"

    return "\n".join([f"{k}: {v}" for k, v in CONTACTS.items()])


def bye(customer_input):
    if customer_input in ("good bye", "exit", "close"):
        return "Good bye"
    raise KeyError


ACTIONS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": get_phone,
    "show": show_all,
    "exit": bye,
    "close": bye,
    "good": bye
}


@input_error
def get_action(customer_input):
    action = customer_input.split()[0]
    return ACTIONS[action]


def main():
    while True:
        customer_input = input(">>>").lower().strip()
        function = get_action(customer_input)
        if not isinstance(function, FunctionType):
            print(function)
            continue
        result = function(customer_input)
        print(result)

        if result == "Good bye!":
            break


if __name__ == '__main__':
    main()
