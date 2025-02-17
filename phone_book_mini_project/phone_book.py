# Empty dict

contacts: dict = {}


def add_contact(name: str, number: int):
    contacts[name] = number


def get_name(name: str):
    return contacts.get(name)


def del_name(name: str):
    if name in contacts:
        del contacts[name]
    else:
        print("Name does not exist")


def display_contact():
    for name, number in contacts.items():
        print(f"{name} {number}")


def edit_contact(name):
    new_number = input("Enter new number: ")
    contacts[name] = new_number


while True:
    print("1. Add Contact \n"
          "2. Get Contact \n"
          "3. Delete Contact \n"
          "4. Display Contact \n"
          "5. Edit Contact \n"
          "6. Press zero to exit \n"
          )

    choice = int(input("Enter your choice = "))

    if choice == 1:
        name1 = input("Enter Name : ")
        number1 = int(input("Enter the phone number = "))

        add_contact(name1, number1)

    elif choice == 2:
        name = input("Enter Name : ")
        get_name(name)

        print(f"The contact number is ", get_name(name))

    elif choice == 3:
        name = input("Enter Name that you want to delete : ")
        del_name(name)

    elif choice == 4:
        display_contact()

    elif choice == 5:
        name1 = input("Enter name to edit Contact: ")

        edit_contact(name1)

    elif choice == 0:
        break

    else:
        print("Invalid .. Please try again...")







