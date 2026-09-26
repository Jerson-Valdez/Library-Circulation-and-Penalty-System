from items import LibraryItem

class Borrower:
    def __init__(self, borrower_id: str, name: str, active_loan_limit: int = 3, loan_history: list = None) -> None:
        self.__borrower_id = borrower_id
        self.__name = name
        self.__active_loan_limit = active_loan_limit
        self.__loan_history = loan_history if loan_history is not None else []

    @property
    def borrower_id(self) -> str:
        return self.__borrower_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def active_loan_limit(self) -> int:
        return self.__active_loan_limit

    @property
    def loan_history(self) -> list:
        return self.__loan_history

    def can_borrow(self) -> bool:
        pass

    def __str__(self):
        return f"Borrower ID: {self.__borrower_id} | Name: {self.__name} | Active Loan Limit: {self.__active_loan_limit} | Loan History: {self.__loan_history}"

    def __eq__(self, other):
        try:
            return self.borrower_id == other.borrower_id
        except AttributeError:
            return False

    def __len__(self) -> int:
        return len(self.__loan_history)


"""-------------------------------------------------LOAN CLASS-------------------------------------------------------"""

class Loan:
    def __init__(self, item: LibraryItem, borrower: Borrower,
                 checkout_day: int, due_day: int, return_day: int = 0,
                 renewal_count: int = 0, status: str = "Active", penalty_amount: float = 0.0) -> None:
        self.__item = item
        self.__borrower = borrower
        self.__checkout_day = checkout_day
        self.__due_day = due_day
        self.__return_day = return_day
        self.__renewal_count = renewal_count
        self.__status = status
        self.__penalty_amount = penalty_amount

    def process_return(self, return_day: int) -> None:
        pass

    def renew_item(self) -> None:
        pass

    def __str__(self):
        return f"Item: {self.__item.title} | Borrower: {self.__borrower.name} | Checkout Day: {self.__checkout_day} | Due Day: {self.__due_day} | Return Day: {self.__return_day} | Renewal Count: {self.__renewal_count} | Status: {self.__status} | Penalty Amount: {self.__penalty_amount}"
