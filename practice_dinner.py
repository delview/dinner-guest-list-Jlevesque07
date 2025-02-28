# practice dinner doc

# 1. If you could invite 6 people to dinner (living or deceased), who would you invite? Make a list that includes these people and use the list to generate a personalized message to each person, inviting them to dinner.
# function to add a person to the dinner guest list
def add_guest(guest: str) -> list:
    """adds a person to the dinner guest list"""
    guest_list.append(guest)
    print(f"{guest}'s message will be: {guest}! You are invited to Joshua's dinner party. Please RSVP with your availability and a dish you would like to be served.")
    return guest_list

# 2. Function to remove a guest from the guest list. 
def replace_guest(guest: str) -> list:
    """Removes a guest from the guest list."""
    guest_list.remove(guest)
    print(f"{guest} has been removed from the guest list. ")
    new_guest = input("Who is the new guest you would like to invite? ").strip().title()
    guest_list.append(new_guest)
    print(f"{new_guest}'s message will be: {new_guest}! You are invited to Joshua's dinner party. Please RSVP with your availability and a dish you would like to be served. ")
    return guest_list


# User menu to access the different guest list functions.
guest_list = []
while True:
    try:
        # Choice that determines what function will be used within the program.
        choice = int(input("What would you like to do with your guest list? [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. "))
        if choice == 1:
            # Option removes a guest from the list and creates their invitation message. It also prints the updated guest list.
            new_guest = input("What is the name of the guest you would like to add? ").strip().title()
            print(f"Your new guest list includes: {add_guest(new_guest)}")
        
        elif choice == 2:
            # Option removes a guest from the list and deletes their invitation message. It also prints the updated guest list.
            while True:
                remove_guest = input("What is the name of the guest you would like to remove? ").strip().title()
                if remove_guest in guest_list:
                    break
                else:
                    print("This person is not in your guest list. ")
            print(f"Your new guest list includes: {replace_guest(remove_guest)}")
        
        elif choice == 3:
            # Option prints the list of invitation messages in alphabetical order.
            guest_list.sort()
            for guest in guest_list:
                print(f"{guest}'s invitation message will be: {guest}! You are invited to Joshua's dinner party. Please RSVP with your availability and a dish you would like to be served. ")
        
        elif choice == 4:
            # Option prints out the number of invited guests.
            print(f"The number of invited guest is {len(guest_list)}")
        
        elif choice == 5:
            exit()
        
        else:
            # Error message for number outside of range 1-5.
            print("Invalid number. Please pick from 1-5 for: [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print Ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. ")

    except ValueError:
        # Error message for non-number input.
        print("Invalid input. Please pick from 1-5 for: [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print Ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. ")
