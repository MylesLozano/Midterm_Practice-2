#Incomplete Phone Book
def add_contacts():
    name = input("Enter contact name: ")
    for i in name:
        if i in name:
            phone_num = int(input("Enter your phone number: "))
            contact_dict.update({name:phone_num})
            print("Contact added successfully.")
            break
        elif i == name:
            print("Already exists!")
            break

# def lookup_contact():

# def delete_contact():

def start_menu():
    print("Phone Book:\n1. Add contact\n2. Look up contact\n3. Delete contact\n4. Exit")
    int(input("Enter your choice: "))

contact_dict = {}
x = 0
start_menu()
match x:
    case 1:
        add_contacts()
        start_menu()
#     case 2:

#     case 3:

#     case 4:
#         exit()