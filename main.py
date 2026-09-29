from manager import LibraryManager
from items import LibraryItem, Book, Magazine, EBook
from transactions import Borrower
from exceptions import LibraryException

def main():

    manager = LibraryManager()
    seed_data(manager)
    while True:
        show_console_menu()
        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                register_item_menu(manager)

            elif choice == 2:
                register_borrower_menu(manager)

            elif choice == 3:
                borrow_item_menu(manager)

            elif choice == 4:
                return_item_menu(manager)

            elif choice == 5:
                renew_item_menu(manager)

            elif choice == 6:
                search_catalog_menu(manager)

            elif choice == 7:
                borrower_history_menu(manager)

            elif choice == 8:
                generate_reports_menu(manager)

            elif choice == 9:
                print("-------------------------------------")
                print("               Goodbye!              ")
                break

            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")


def show_console_menu():
    print("-------------------------------------")
    print("       Welcome to the library!       ")
    print("-------------------------------------")
    print("Enter your choice to the console menu")
    print("1) Register item")
    print("2) Register borrower")
    print("3) Borrow item")
    print("4) Return item")
    print("5) Renew item")
    print("6) Search Catalog")
    print("7) Show Borrower History")
    print("8) Generate reports")
    print("9) Exit")

def generate_reports_menu(manager: LibraryManager) -> None:
    try:
        current_day = int(input("Enter current day: "))

    except ValueError:
        print("Please enter a valid number.")
    else:
        reports = manager.generate_reports(current_day)

        print("\nAvailable Items by Type")

        for item_type, items in reports["available_items"].items():
            print(f"\n{item_type}:")
            for item in items:
                print(f"  {item}")

        print("\nActive Loans")

        for loan in reports["active_loans"]:
            print(loan)

        print("\nOverdue Loans")

        for loan in reports["overdue_loans"]:
            print(loan)

        print("\nAccumulated Penalties")

        for borrower, penalty in reports["penalties"].items():
            print(f"{borrower}: ${penalty:.2f}")

        print("\nBorrow Frequency By Resource Type")

        for resource_type, count in reports["most_borrowed"]:
            print(f"{resource_type}: {count}")
    finally:
        print("-------------------------------------")
        print("Report generation attempt completed.")

def borrower_history_menu(manager: LibraryManager) -> None:
    while True:
        try:
            print("           Borrower history          ")
            print("-------------------------------------")
            borrower_id = input("Enter borrower id: ")
            loans = manager.show_borrower_history(borrower_id)
            for loan in loans:
                print(loan)
        except LibraryException as e:
            print(e)

        choice = input("\nInput again? (y/n): ").lower()

        if choice == "n":
            return


def search_catalog_menu(manager: LibraryManager) -> None:
    while True:
        print("            Search Catalog           ")
        print("-------------------------------------")
        keyword = input("Search catalog: ")

        results = manager.search_catalog(keyword)

        if not results:
            print("No items found.")
        else:
            for result in results:
                print(result)

        choice = input("\nSearch again? (y/n): ").lower()

        if choice == "n":
            return


def renew_item_menu(manager: LibraryManager) -> None:
    while True:
        print("             Renew Item              ")
        print("-------------------------------------")
        try:
            borrower_id = input("Enter borrower id: ")

            if not manager.borrower_exists(borrower_id):
                print("Borrower does not exists!")
                continue

            item_code = input("Enter item code: ")

            if not manager.item_exists(item_code):
                print("Item does not exists!")
                continue

            manager.renew_item(
                borrower_id=borrower_id,
                item_code=item_code
            )
        except LibraryException as e:
            print(e)
            print("Continue or return to main menu?")
            print("1) Continue")
            print("2) Return to main menu")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                continue
            elif choice == "2":
                return
            else:
                print("Invalid choice!")
        else:
            print("Loan renewed successfully!")
            break


def return_item_menu(manager: LibraryManager) -> None:

    while True:
        print("            Return Item              ")
        print("-------------------------------------")
        try:
            borrower_id = input("Enter borrower id: ")

            if not manager.borrower_exists(borrower_id):
                print("Borrower does not exists!")
                continue

            item_code = input("Enter item code: ")

            if not manager.item_exists(item_code):
                print("Item does not exists!")
                continue

            day = int(input("Enter day: "))

            manager.return_item(
                borrower_id=borrower_id,
                item_code=item_code,
                day=day
            )
        except LibraryException as e:
            print(e)
            print("Continue or return to main menu?")
            print("1) Continue")
            print("2) Return to main menu")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                continue
            elif choice == "2":
                return
            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid choice!")
        else:
            print("Item Returned successfully!")
            break


def borrow_item_menu(manager: LibraryManager) -> None:
    while True:
        print("            Borrow Item              ")
        print("-------------------------------------")
        try:
            borrower_id = input("Enter borrower id: ")

            if not manager.borrower_exists(borrower_id):
                print("Borrower does not exists!")
                continue

            item_code = input("Enter item code: ")

            if not manager.item_exists(item_code):
                print("Item does not exists!")
                continue

            day = int(input("Enter day: "))

            manager.borrow_item(
                borrower_id=borrower_id,
                item_code=item_code,
                day=day
            )

        except LibraryException as e:
            print(e)
            print("Continue or return to main menu?")
            print("1) Continue")
            print("2) Return to main menu")
            choice = input ("\nEnter your choice: ")
            if choice == "1":
                continue
            elif choice == "2":
                return
            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid choice!")
            continue
        else:
            print("Item borrowed successfully!")
            break


def register_borrower_menu(manager: LibraryManager) -> None:
    while True:
        print("          Register Borrower          ")
        print("-------------------------------------")
        try:
            borrower_id = input("Enter borrower id: ")

            if manager.borrower_exists(borrower_id):
                print("Borrower already exists!")
                continue

            name = input("Enter borrower name: ")

            borrower = Borrower(borrower_id, name)
            manager.register_borrower(borrower)

        except LibraryException as e:
            print(e)
            print("Continue or return to main menu?")
            print("1) Continue")
            print("2) Return to main menu")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                continue
            elif choice == "2":
                return
            else:
                print("Invalid choice!")
        else:
            print("Borrower registered successfully!")
            break


def register_item_menu(manager: LibraryManager):
    while True:

        print("            Register Item            ")
        print("-------------------------------------")
        print("Select item type:")
        print("1) Book")
        print("2) EBook")
        print("3) Magazine")
        print("4) Return to main menu")

        try:
            item = input("\nEnter your choice: ")

            if item == "1":
                item_code = input("Enter item code: ")

                if manager.item_exists(item_code):
                    print("Item already exists!")
                    continue

                title = input("Enter item title: ")

                item_obj = Book(
                    item_code=item_code,
                    title=title
                )

            elif item == "2":
                item_code = input("Enter item code: ")

                if manager.item_exists(item_code):
                    print("Item already exists!")
                    continue

                title = input("Enter item title: ")
                digital_rules = input("Enter Digital rules: ")
                item_obj = EBook(
                    item_code=item_code,
                    title=title,
                    digital_rules=digital_rules
                )

            elif item == "3":
                item_code = input("Enter item code: ")

                if manager.item_exists(item_code):
                    print("Item already exists!")
                    continue

                title = input("Enter item title: ")

                item_obj = Magazine(
                    item_code=item_code,
                    title=title
                )

            elif item == "4":
                return
            else:
                print("Invalid choice!")
                continue
        except LibraryException as e:
            print(e)
            print("Continue or return to main menu?")
            print("1) Continue")
            print("2) Return to main menu")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                continue
            elif choice == "2":
                return
            else:
                print("Invalid choice!")
        else:
            manager.register_item(item_obj)
            print("Item registered successfully!")
            return

def seed_data(manager: LibraryManager) -> None:
    manager.register_item(Book("B001", "The Chronicles of the Sea"))
    manager.register_item(Book("B002", "Python Programming"))
    manager.register_item(Book("B003", "Clean Code"))

    manager.register_item(Magazine("M001", "Tech Monthly"))
    manager.register_item(Magazine("M002", "Science Today"))

    manager.register_item(
        EBook("E001", "Django Fundamentals", "Digital access only")
    )

    manager.register_borrower(Borrower("BR001", "John"))
    manager.register_borrower(Borrower("BR002", "Mary"))
    manager.register_borrower(Borrower("BR003", "Alex"))
    manager.register_borrower(Borrower("BR004", "Sarah"))

if __name__ == "__main__":
    main()





