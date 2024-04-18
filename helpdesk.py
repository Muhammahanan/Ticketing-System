class HelpDesk:
    def __init__(self):
        # Initialize the HelpDesk with empty dictionaries to store ticket information
        self.tickets = {}  # Dictionary to store ticket details
        self.ticket_counter = 2000  # Initial ticket ID counter
        self.open_tickets_count = 0  # Count of open tickets
        self.total_tickets_count = 0  # Total count of tickets
        self.resolved_tickets_count = 0  # Count of resolved tickets

    # Main menu function to interact with the HelpDesk class
    def main_menu(self):
        while True:
            print("\nHELP DESK TICKETING SYSTEM")
            print("1. SUBMIT A TICKET")  # Option to submit a new ticket
            print("2. VIEW TICKET")  # Option to view an existing ticket
            print("3. LIST TICKETS")  # Option to list all tickets
            print("4. RESPOND TO A TICKET")  # Option to respond to a ticket
            print("5. REOPEN A TICKET")  # Option to reopen a closed ticket
            print("6. SHOW TICKET STATUS")  # Option to show the status of tickets
            print("7. VIEW TICKET STATISTICS")  # Option to view statistics
            print("8. EXIT")  # Option to exit the application
            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                self.submit_ticket_menu()
            elif choice == "2":
                self.view_ticket_menu()
            elif choice == "3":
                self.list_tickets_menu()
            elif choice == "4":
                self.respond_to_ticket_menu()
            elif choice == "5":
                self.reopen_ticket_menu()
            elif choice == "6":
                self.show_ticket_status_menu()
            elif choice == "7":
                self.view_ticket_statistics_menu()
            elif choice == "8":
                print("Exiting the Help Desk Ticketing System.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    # Function to submit a new ticket
    def submit_ticket_menu(self):
        print("\nSUBMIT A TICKET")
        requester_name = input("Enter your name: ")
        staff_id = input("Enter your staff ID: ")
        email = input("Enter your email address: ")
        issue_description = input("Describe the issue: ")
        self.submit_ticket(requester_name, staff_id, email, issue_description)

    # Function to view an existing ticket
    def view_ticket_menu(self):
        print("\nVIEW TICKET")
        ticket_number = int(input("Enter the ticket number: "))
        print(self.view_ticket(ticket_number))

    # Function to list all tickets
    def list_tickets_menu(self):
        print("\nLIST TICKETS")
        print(self.list_tickets())

    # Function to respond to a ticket
    def respond_to_ticket_menu(self):
        print("\nRESPOND TO A TICKET")
        ticket_number = int(input("Enter the ticket number: "))
        response = input("Enter your response: ")
        self.respond_to_ticket(ticket_number, response)

    # Function to reopen a closed ticket
    def reopen_ticket_menu(self):
        print("\nREOPEN A TICKET")
        ticket_number = int(input("Enter the ticket number: "))
        self.reopen_ticket(ticket_number)

    # Function to show the status of tickets
    def show_ticket_status_menu(self):
        print("\nSHOW TICKET STATUS")
        print(self.show_ticket_status())

    # Function to view ticket statistics
    def view_ticket_statistics_menu(self):
        print("\nVIEW TICKET STATISTICS")
        print(self.view_ticket_statistics())

    # Function to submit a new ticket
    def submit_ticket(self, Hanan, staff_id, email, issue_description):
        ticket_number = self.ticket_counter
        # Store ticket details in the tickets dictionary
        self.tickets[ticket_number] = {
            'requester_name': Hanan,
            'staff_id': 1234,
            'email': email,
            'issue_description': issue_description,
            'response': "Good to go",
            'status': 'Open'
        }
        self.ticket_counter += 1  # Increment ticket counter
        self.open_tickets_count += 1  # Increment open tickets count
        self.total_tickets_count += 1  # Increment total tickets count
        print(f'Ticket ID {ticket_number} created successfully.')

    # Function to view an existing ticket
    def view_ticket(self, ticket_number):
        ticket = self.tickets.get(ticket_number)
        if ticket:
            return f'Ticket ID: {ticket_number}\nRequester Name: {ticket["requester_name"]}\nStaff ID: {ticket["staff_id"]}\nE-mail: {ticket["email"]}\nIssue Description: {ticket["issue_description"]}\nResponse: {ticket["response"]}\nStatus: {ticket["status"]}'
        else:
            return f'Ticket ID {ticket_number} not found.'

    # Function to list all tickets
    def list_tickets(self):
        if self.tickets:
            return '\n'.join([f'Ticket ID: {k} - Status: {v["status"]}' for k, v in self.tickets.items()])
        else:
            return 'No tickets found.'

    # Function to respond to a ticket
    def respond_to_ticket(self, ticket_number, response):
        ticket = self.tickets.get(ticket_number)
        if ticket:
            ticket['response'] = response
            ticket['status'] = 'Closed'
            self.open_tickets_count -= 1  # Decrement open tickets count
            self.resolved_tickets_count += 1  # Increment resolved tickets count
            print(f'Ticket ID {ticket_number} closed successfully.')
        else:
            print(f'Ticket ID {ticket_number} not found.')

    # Function to reopen a closed ticket
    def reopen_ticket(self, ticket_number):
        ticket = self.tickets.get(ticket_number)
        if ticket:
            ticket['status'] = 'Reopened'
            self.open_tickets_count += 1  # Increment open tickets count
            self.resolved_tickets_count -= 1  # Decrement resolved tickets count
            print(f'Ticket ID {ticket_number} reopened successfully.')
        else:
            print(f'Ticket ID {ticket_number} not found.')

    # Function to show the status of tickets
    def show_ticket_status(self):
        return f"Total Tickets: {self.total_tickets_count}\nOpen Tickets: {self.open_tickets_count}"

    # Function to view ticket statistics
    def view_ticket_statistics(self):
        return f"Total Tickets: {self.total_tickets_count}\nResolved Tickets: {self.resolved_tickets_count}\nOpen Tickets: {self.open_tickets_count}"


# Main program starts here
if __name__ == "__main__":
    # Create an instance of the HelpDesk class
    help_desk = HelpDesk()
    # Start the main menu
    help_desk.main_menu()
