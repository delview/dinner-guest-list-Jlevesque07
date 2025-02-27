# practice dinner doc

# 1. If you could invite 6 people to dinner (living or deceased), who would you invite? Make a list that includes these people and use the list to generate a personalized message to each person, inviting them to dinner.
# function to add a person to the dinner guest list, and create a message for that, which is added to the message list
def add_guest(guest: str) -> list:
    """adds a person to the dinner guest list, and create a message for that, which is added to the message list"""
    invitee_list.append(guest)
    guests_message = (f"{guest}! You are invited to Joshua's dinner party. Please RSVP with your availability and a dish you would like to be served. ")
    print(f"{guest}'s message will be: {guests_message}")
    message_list.append(guests_message)
    return invitee_list

# 2. Function to remove a guest and their greeting message, then ask for a new guest. The new guest and their message will be added to their respective lists. 
def replace_guest(guest: str) -> list:
    """remove a guest and their greeting message, then ask for a new guest. The new guest and their message will be added to their respective lists."""
    invitee_list.remove(guest)
    message_list.remove(person for person in message_list if guest in person)
    new_guest = input("Who is the new guest you would like to invite? ").strip().title()
    invitee_list.append(new_guest)
    guests_message = (f"{new_guest}! You are invited to Joshua's dinner party. Please RSVP with your availability and a dish you would like to be served. ")
    print(f"{new_guest}'s message will be: {guests_message}")
    message_list.append(guests_message)
    return invitee_list


# User menu to access the different dinner list functions.
invitee_list = []
message_list = []
while True:
    try:
        # Choice that determines what function will be used within the program.
        choice = int(input("What would you like to do with your dinner list? [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. "))
        if choice == 1:
            # Option removes a guest from the list and creates their invitation message. It also prints the updated invitee list.
            new_guest = input("What is the name of the guest you would like to add? ").strip().title()
            print(f"Your new dinner list includes: {add_guest(new_guest)}")
        
        elif choice == 2:
            # Option removes a guest from the list and deletes their invitation message. It also prints the updated invitee list.
            remove_guest = input("What is the name of the guest you would like to remove? ").strip().title()
            print(f"Your new dinner list includes: {replace_guest(remove_guest)}")
        elif choice == 3:
            # Option prints the list of invitation messages in alphabetical order.
            message_list.sort()
            print(f"Your list of invitations: {message_list}")
        elif choice == 4:
            # Option prints out the number of invited guests.
            print(f"The number of invited guest is {len(message_list)}")
        elif choice == 5:
            exit()
        
        else:
            # Error message for number outside of range 1-5.
            print("Invalid number. Please pick from 1-5 for: [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print Ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. ")
    except ValueError:
        # Error message for non-number input.
        print("Invalid input. Please pick from 1-5 for: [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print Ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. ")
