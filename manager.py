from items import LibraryItem
from transactions import Borrower, Loan
from exceptions import LibraryException

class LibraryManager:
    def __init__(self):
        self.__catalog = {}
        self.__borrowers = {}
        self.__loans = []

    def borrower_exists(self, borrower_id: str) -> bool:
        return borrower_id in self.__borrowers

    def item_exists(self, item_code: str) -> bool:
        return item_code in self.__catalog

    def register_item(self, item: LibraryItem) -> None:
        if item.item_code in self.__catalog:
            raise LibraryException("Item already registered!")

        self.__catalog[item.item_code] = item

    def register_borrower(self, borrower: Borrower) -> None:
        if borrower.borrower_id in self.__borrowers:
            raise LibraryException("Borrower already registered!")

        self.__borrowers[borrower.borrower_id] = borrower


    def borrow_item(self, borrower_id: str, item_code: str, day: int) -> None:
        borrower = self.__borrowers.get(borrower_id)

        if borrower is None:
            raise LibraryException("Borrower not registered!")

        item = self.__catalog.get(item_code)

        if item is None:
            raise LibraryException("Item not registered!")

        if not item.is_available:
            raise LibraryException("Item is currently unavailable!")

        if not borrower.can_borrow():
            raise LibraryException("Borrower has already reached the active loan limit!")

        due_day = day + item.get_loan_period()

        loan = Loan(
            item=item,
            borrower=borrower,
            checkout_day=day,
            due_day=due_day,
        )

        item.is_available = False
        self.__loans.append(loan)
        borrower.loan_history.append(loan)
        return


    def return_item(self, borrower_id: str, item_code: str, day: int) -> None:
        borrower = self.__borrowers.get(borrower_id)

        if borrower is None:
            raise LibraryException("Borrower not registered!")

        item = self.__catalog.get(item_code)

        if item is None:
            raise LibraryException("Item not registered!")

        for loan in self.__loans:
            if (loan.borrower == borrower and
                    loan.item == item and
                    loan.status == "Active"
            ):
                loan.process_return(day)
                item.is_available = True
                return

        raise LibraryException("No active loan found for this borrower and item!")


    def renew_item(self, borrower_id: str, item_code: str) -> None:
        borrower = self.__borrowers.get(borrower_id)

        if borrower is None:
            raise LibraryException("Borrower not registered!")

        item = self.__catalog.get(item_code)

        if item is None:
            raise LibraryException("Item not registered!")

        for loan in self.__loans:
            if (loan.borrower == borrower and
                    loan.item == item and
                    loan.status == "Active"):

                loan.renew_item()
                return

        raise LibraryException("No active loan found for this borrower and item!")

    def search_catalog(self, keyword:str) -> list:
        results = []

        keyword = keyword.lower()

        for item in self.__catalog.values():
            if (
                    keyword in item.item_code.lower()
                    or keyword in item.title.lower()
            ):
                results.append(item)

        return results


    def show_borrower_history(self, borrower_id: str) -> list:

        borrower = self.__borrowers.get(borrower_id)

        if borrower is None:
            raise LibraryException("Borrower not registered!")

        if not borrower.loan_history:
            raise LibraryException("This borrower has no loan history yet!")

        return borrower.loan_history

    def generate_reports(self, current_day: int) -> dict:
        available_items = {}

        for item in self.__catalog.values():
            if item.is_available:
                resource_type = item.get_resource_type()

                if resource_type not in available_items:
                    available_items[resource_type] = []

                available_items[resource_type].append(item)

        active_loans = [
            loan for loan in self.__loans if loan.status == "Active"
        ]

        overdue_loans = [
            loan for loan in self.__loans if loan.status == "Active" and loan.due_day < current_day
        ]

        penalties = {}

        for loan in self.__loans:
            borrower_id = loan.borrower.borrower_id

            penalties[borrower_id] = (
                penalties.get(borrower_id, 0) + loan.penalty_amount
            )

        borrow_counts = {}

        for loan in self.__loans:
            resource_type = loan.item.get_resource_type()

            borrow_counts[resource_type] = (
                borrow_counts.get(resource_type, 0) + 1
            )

        most_borrowed = sorted(
            borrow_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return {
            "available_items": available_items,
            "active_loans": active_loans,
            "overdue_loans": overdue_loans,
            "penalties": penalties,
            "most_borrowed": most_borrowed
        }

    def __str__(self):
        return (
            f"Library Manager | "
            f"Items: {len(self.__catalog)} | "
            f"Borrowers: {len(self.__borrowers)} | "
            f"Loans: {len(self.__loans)}"
        )

    def __len__(self):
        return len(self.__catalog)

