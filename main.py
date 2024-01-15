CONTACTS = {}


def input_error(func):
    def inner(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                return result
            except (KeyError, TypeError, ValueError):
                return "Incorrect value. Please, try again."

    return inner


def handler(action):
    return ACTIONS[action]

@input_error
def hello():
    return "How can I help you?"


@input_error
def add(name, phone):
    if not CONTACTS.get(name):
        CONTACTS[name] = phone
        return "Thank you!"
    return "Contact with such name already exists."

@input_error
def change(name, phone):
    if CONTACTS[name]:
        CONTACTS[name] = phone
        return "Thank you!"
    return ""


@input_error
def phone(name):
    return CONTACTS[name]

@input_error
def show_all():
    if len(CONTACTS) > 0:
        for k, v in CONTACTS.items():
            return f"{k}: {v}"

    return "Empty contacts library."


ACTIONS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show": show_all
}

def main():
    while True:
        customer_input = input().split()
        action = customer_input[0].lower()

        if action in ("add", "change"):
            name, phone = customer_input[-2:]
            result = handler(action)
            print(result(name, phone))

        elif action in ("phone"):
            name = customer_input[-1]
            result = handler(action)
            print(result(name))

        elif action == "hello" or (action == "show" and customer_input[1].lower() == "all"):
            result = handler(action)
            print(result())

        elif action in ("close", "exit", ".") or \
                (action == "good" and customer_input[1].lower() == "bye"):
            print("Good bye!")
            break

        if action not in ACTIONS:
            print("Unknown action. Please, try again.")


if __name__ == '__main__':
    main()
