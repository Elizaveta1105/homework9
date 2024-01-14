CONTACTS = {}


def input_error(func):
    def inner(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                return result
            except ValueError:
                print("Sorry, I don't understand you. Please retype your request.\n")

    return inner


def handler(action):
    return ACTIONS[action]

def hello():
    print("How can I help you?")


def add(name, phone):
    CONTACTS[name] = phone


def change(name, phone):
    CONTACTS[name] = phone


def phone(name):
    print(CONTACTS[name])


def show_all():
    for k, v in CONTACTS.items():
        print(f"{k}: {v}")


ACTIONS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all
}


@input_error
def main():
    while True:
        action = input().lower()

        if action in ("add", "change"):
            name, phone = input('Give me your name and phone via space \n').split()
            result = handler(action)
            result(name, phone)
            print("Thank you! I received your data.")

        elif action in ("phone"):
            name = input('Enter username \n')
            result = handler(action)
            result(name)

        elif action in ("show all", "hello"):
            result = handler(action)
            result()

        elif action in ("close", "exit", "good bye", "."):
            print("Good bye!")
            return

        if action not in ACTIONS:
            raise ValueError



if __name__ == '__main__':
    main()
