class Ticket:
    def __init__(self, ticket_num, ticket_creator_name, staff_id, contact_email, description, response="Not Yet Provided", status="Open"):
        self.ticket_num = ticket_num
        self.ticket_creator_name = ticket_creator_name
        self.staff_id = staff_id
        self.contact_email = contact_email
        self.description = description
        self.response = response
        self.status = status

    def resolve_password_change(self):
        if "Password change" in self.description:
            new_password = self.staff_id[:2] + self.ticket_creator_name[:3]
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"


class TicketingSystem:
    def __init__(self):
        self.tickets = []
        self.next_ticket_num = 2000

    def submit_ticket(self, ticket_creator_name, staff_id, contact_email, description):
        new_ticket_num = self.next_ticket_num
        self.next_ticket_num += 1
        ticket = Ticket(new_ticket_num, ticket_creator_name, staff_id, contact_email, description)
        ticket.resolve_password_change()  # Check if it's a password change request
        self.tickets.append(ticket)
        print(f"Ticket ID: {ticket.ticket_num} - Ticket submitted successfully.")

    def display_tickets(self):
        if not self.tickets:
            print("No tickets to display.")
            return

        print("************Display Tickets *********************")
        for ticket in self.tickets:
            print(f"Ticket Number: {ticket.ticket_num}")
            print(f"Ticket Creator: {ticket.ticket_creator_name}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Contact Email: {ticket.contact_email}")
            print(f"Description: {ticket.description}")
            print(f"Response: {ticket.response}")
            print(f"Status: {ticket.status}")
            print()

    def ticket_statistics(self):
        created = len(self.tickets)
        resolved = sum(1 for ticket in self.tickets if ticket.status == "Closed")
        to_solve = sum(1 for ticket in self.tickets if ticket.status != "Closed")

        print("***************Displaying Ticket Statistics*************\n")
        print(f"Tickets Created: {created}")
        print(f"Tickets Resolved: {resolved}")
        print(f"Tickets To Solve: {to_solve}")

    def resolve_ticket(self, ticket_num, response):
        found = False
        for ticket in self.tickets:
            if ticket.ticket_num == ticket_num:
                ticket.response = response
                ticket.status = "Closed"
                print("Ticket resolved successfully.")
                found = True
                break
        if not found:
            print("Ticket not found.")

    def reopen_ticket(self, ticket_num):
        found = False
        for ticket in self.tickets:
            if ticket.ticket_num == ticket_num:
                ticket.status = "Reopened"
                print("Ticket reopened successfully.")
                found = True
                break
        if not found:
            print("Ticket not found.")


def main():
    ticketing_system = TicketingSystem()
    print("\n***********************************")
    print("Help Desk Ticketing management")
    print("\n***********************************")

    while True:
        print("\nMenu:")
        print("1. Submit Ticket")
        print("2. Display Tickets")
        print("3. Ticket Statistics")
        print("4. Resolve Ticket")
        print("5. Reopen Ticket")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n************Create a new Ticket*************")
            ticket_creator_name = input("Enter ticket creator's name: ")
            staff_id = input("Enter staff ID: ")
            contact_email = input("Enter contact email: ")
            description = input("Enter issue description: ")
            ticketing_system.submit_ticket(ticket_creator_name, staff_id, contact_email, description)

        elif choice == "2":
            ticketing_system.display_tickets()

        elif choice == "3":
            ticketing_system.ticket_statistics()

        elif choice == "4":
            ticket_num = int(input("\nEnter ticket number to resolve: "))
            response = input("Enter response: ")
            ticketing_system.resolve_ticket(ticket_num, response)

        elif choice == "5":
            ticket_num = int(input("Enter ticket number to reopen: "))
            ticketing_system.reopen_ticket(ticket_num)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()
