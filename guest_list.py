# 1. If you could invite 6 people to dinner (living or deceased), who would you invite? Make a list that includes these people and use the list to generate a personalized message to each person, inviting them to dinner.

# function to add a person to the dinner guest list, and create a message for the added person
def add_guest(guest: str) -> list:
    invitee_list.append(guest)
    print(f"{guest}'s message will be: {guest}! You are invited to Joshua's dinner party. Please RSVP with your availability and a dish you would like to be served. ")
    return invitee_list

# 2. You just found out that one of your dinner guests can't make it so you need to find someone different to invite and send out new invitations. Create a program that will replace the guest who can't make it with the new guest and regenerate your invitations.

# 3. Use sort() in your code to print out the invitations to your guests in alphabetical order by their names.

# 4. Use len() in your code to print out the number of dinner guests invited by figuring out the length of the list.

# User menu to access the different dinner list functions.
invitee_list = []
message_list = []
while True:
    try:
        # Choice that determines what function will be used within the program.
        choice = int(input("What would you like to do with your dinner list? [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print Ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. "))
        if choice == 1:
            # Option removes a guest from the list and creates their invitation message. It also prints the updated invitee list.
            new_guest = input("What is the name of the guest you would like to add? ").strip().title()
            print(f"Your new dinner list includes: {add_guest(new_guest)}")
        
        elif choice == 2:
            # Option removes a guest from the list and deletes their invitation message. It also prints the updated invitee list.

        elif choice == 3:
            # Option prints the list of invitation messages in alphabetical order.

        elif choice == 4:
            # Option prints out the number of invited guests.

        elif choice == 5:
            exit()
        
        else:
            print("Invalid number. Please pick from 1-5 for: [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print Ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. ")
    except ValueError:
        print("Invalid input. Please pick from 1-5 for: [1] Add a person to the list & make them an invitation, [2] Remove a person from the list, [3] Print Ivitation messages, [4] Print out the number of guests invited, [5] Exit the program. ")

