# Dinner Party Assignment



#Function to add a person to the guest list until variable for number of people who are going to be invited is zero
def add() -> list:
    """Adds a chosen number of people to "guest_list", and states the new list of invitees. """
    
    while True:
        
        try:
            num_guests = int(input("How many guests do you want to invite? "))
            
            if num_guests > 0:
                break
            elif num_guests == 0:
                return guest_list
            else:
                print("Please pick a positive number, or zero for no guests. ")
        
        except ValueError:
            print("Please input a number. ")


    while num_guests > 0:
        new_guest = input("Who is the guest you would like to add? ").strip().title()
        guest_list.append(new_guest)
        num_guests = num_guests - 1
    
    print(f"Your new guest list includes: {guest_list}.")
    return guest_list


# Function to remove a person from the guest list and replace them with a new guest.
def rar(guest: str) -> list:
    """Removes a person from the guest list and replaces them with a new guest. """


guest_list = []
while True:
    option = input("Would you like to: Add people to the list? [1], Replace someone in the list? [2], Print out a list of the invitations that will be sent out? [3], Exit the program? [4]")
    
    if int(option) == 1:
        # Function "add" called. Adds a chosen number of people to "guest_list"
        add()

    elif int(option) == 2:
        # Function remove_and_replace (rar) called. 

    elif int(option) == 3:
        # Print out invitations for each dinner guest. 

    elif int(option == 4):
        # Exit the program.

