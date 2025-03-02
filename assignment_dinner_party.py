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
        print(f"{new_guest} added to the guest list. ")
        num_guests = num_guests - 1
    
    print(f"Your new guest list includes: {guest_list}.")
    return guest_list


# Function to remove a person from the guest list and replace them with a new guest.
def rar(guest: str) -> list:
    """Removes a person from the guest list and replaces them with a new guest. """
    guest_list.remove(guest)
    print(f"{guest} removed from the guest list. ")
    new_guest = input("Who would you like to add to the guest list? ").strip().title()
    guest_list.append(new_guest)
    print(f"{new_guest} added to the guest list. ")
    print(f"Your new guest list includes: {guest_list}.")
    return guest_list



guest_list = []
while True:
    # Different option values (1-4) call different functions.
    option = input("Would you like to: Add people to the list? [1], Replace someone in the list? [2], Print out a list of the invitations that will be sent out? [3], Exit the program? [4] ").strip()
    
    if option == "1": 
        add()
    
    elif option == "2":
        remove = 1
        while remove == 1:
            rem_guest = input("Who is the person you would like to remove from the guest list? ").strip().title()
            
            if rem_guest in guest_list:
                rar(rem_guest)
                remove = 0
            else:
                while True:
                    choice = input("Whoops! It seems this guest isn't in the list. Would you like to try again? [1], or go back to the menu? [2] ").strip()
                    if choice == "1":
                        break
                    elif choice == "2":
                        remove = 0
                        break
                    else:
                        print("Please choose 1 or 2. ")

    elif option == "3":
        # Print out invitations for each dinner guest. 
        print("Your guest invitations: ")
        for guest in guest_list:
            print(f"{guest}! you are invited to Joshua's dinner party. ")

    elif option == "4":
        # Exit the program.
        exit()
    
    else: 
        # Improper input fallback.
        print("Please pick a number from 1-4. ")

