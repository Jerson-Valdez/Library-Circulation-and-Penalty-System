from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_code: str, title: str, is_available: bool = True) -> None:
        self.__item_code = item_code
        self.__title = title
        self.__is_available = is_available

    @abstractmethod
    def get_resource_type(self) -> str:
        pass

    @property
    def item_code(self) -> str:
        return self.__item_code

    @property
    def title(self) -> str:
        return self.__title

    @property
    def is_available(self) -> bool:
        return self.__is_available

    @is_available.setter
    def is_available(self, status: bool) -> None:
        self.__is_available = status

    @abstractmethod
    def get_loan_period(self) -> int:
        pass

    @abstractmethod
    def calculate_penalty(self, days_overdue: int) -> float:
        pass

    def __str__(self) -> str:
        return f"Item Code: {self.__item_code} | Title: {self.__title} | Available: {self.__is_available}"

    def __eq__(self, other) -> bool:
        try:
            return self.item_code == other.item_code
        except AttributeError:
            return False


"""-----------------------------------------------EBOOOK SUBCLASS----------------------------------------------------"""
# yung digital_rules d ako sure kung ano need na datatype
# and kung pano sya irereturn or ilalagay sa system HAHAHHA

class EBook(LibraryItem):
    def __init__(self, item_code: str, title: str, digital_rules: str, is_available: bool = True) -> None:
        super().__init__(item_code, title, is_available)
        self.__digital_rules = digital_rules

    @property
    def digital_rules(self):
        return self.__digital_rules

    def get_loan_period(self) -> int:
        return 14

    def calculate_penalty(self, days_overdue: int) -> float:
        if days_overdue > 0:
            return float(days_overdue * 10.0)
        return 0.0

    def get_resource_type(self) -> str:
        return "EBook"


"""------------------------------------------------BOOK SUBCLASS-----------------------------------------------------"""

class Book(LibraryItem):
    def __init__(self, item_code: str, title: str, penalty_rate : float = 5.0, is_available: bool = True) -> None:
        super().__init__(item_code, title, is_available)
        self.__penalty_rate = penalty_rate

    @property
    def penalty_rate(self):
        return self.__penalty_rate

    def get_loan_period(self) -> int:
        return 7

    def calculate_penalty(self, days_overdue : int) -> float:
        if days_overdue > 0:
            return float(days_overdue * self.penalty_rate)
        return 0.0

    def get_resource_type(self) -> str:
        return "Book"

"""----------------------------------------------MAGAZINE SUBCLASS---------------------------------------------------"""

class Magazine(LibraryItem):
    def __init__(self, item_code: str, title: str, penalty_rate : float = 20.0, is_available: bool = True) -> None:
        super().__init__(item_code, title, is_available)
        self.__penalty_rate = penalty_rate

    @property
    def penalty_rate(self):
        return self.__penalty_rate

    def get_loan_period(self) -> int:
        return 3

    def calculate_penalty(self, days_overdue : int) -> float:
        if days_overdue > 0:
            return float(days_overdue * self.penalty_rate)
        return 0.0

    def get_resource_type(self) -> str:
        return "Magazine"