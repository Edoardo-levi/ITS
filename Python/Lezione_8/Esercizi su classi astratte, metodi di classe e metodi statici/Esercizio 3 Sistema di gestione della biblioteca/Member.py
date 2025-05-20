from Book import Book
from typing import Self

class Member:
    def __init__(self, name:str, member_id:str):
        self._name=name
        self._member_id=member_id
        self._borrow_book:list[Book]= []

    def borrow_book (self, book:Book)->None:
        self._borrow_book.append(book)

    def return_book (self,book:Book)->None:
        if book in self.borrow_book:
            self._borrow_book.remove(book)

    def __str__(self) ->str:
        return f"Name= {self._name}; Member ID = {self._member_id}"
    
    @classmethod
    def from_string (cls, in_str:str)-> Self:
        subs = in_str.split(',')
        return cls(subs[0],subs[1])