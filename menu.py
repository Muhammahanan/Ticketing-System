# Define the main menu function to interact with the HelpDesk class
def main_menu():
    while True:
        print("")  # Print an empty line for better formatting
        print("MAIN MENU")  # Display the main menu title
        print("1. SUBMIT A TICKET")  # Option to submit a new ticket
        print("   - Submit a ticket for assistance from the Help Desk.")
        print("2. VIEW TICKET")  # Option to view an existing ticket
        print("   - View detailed information about an existing ticket.")
        print("3. LIST TICKETS")  # Option to list all tickets
        print("   - List all tickets along with their statuses.")
        print("4. RESPOND TO A TICKET")  # Option to respond to a ticket
        print("   - Respond to a ticket and mark it as closed.")
        print("5. REOPEN A TICKET")  # Option to reopen a closed ticket
        print("   - Reopen a previously closed ticket.")
        print("6. SHOW STATUS")  # Option to show the status of tickets
        print("   - Display the total number of tickets and open tickets.")
        print("7. EXIT")  # Option to exit the application
        print("   - Exit the application.")
        # Prompt for user choice
        print("Please choose an option between 1 and 7.")
        print("")
        choice = input("YOUR CHOICE: ")  # Get user's choice

# Test the main menu function
main_menu()
