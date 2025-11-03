"""Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

Classe Book:

Attributi:
book_id: str - Identificatore di un libro.
title: str - titolo del libro.
author: str - autore del libro
is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
Metodi:
borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
return_book()- Contrassegna il libro come restituito.
Classe Member:

Attributi:
member_id: str - identificativo del membro.
name: str - il nome del membro.
borrowed_books: list[Book] - lista dei libri presi in prestito.
Metodi:
borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
return_book(book): rimuove il libro dalla lista borrowed_books.
Classe Library:

Attributi:
books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
Metodi:
add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro."""

class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise ValueError("Book is already borrowed")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError("Book is not borrowed")
        self.is_borrowed = False


class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise ValueError("Book not borrowed by this member")
        book.return_book()
        self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = {}    # key: book_id, value: Book
        self.members = {}  # key: member_id, value: Member

    def add_book(self, book_id: str, title: str, author: str):
        if book_id in self.books:
            raise ValueError(f"Book with ID {book_id} already exists")
        self.books[book_id] = Book(book_id, title, author)

    def register_member(self, member_id: str, name: str):
        if member_id in self.members:
            raise ValueError(f"Member with ID {member_id} already exists")
        self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id: str, book_id: str):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")

        member = self.members[member_id]
        book = self.books[book_id]
        member.borrow_book(book)

    def return_book(self, member_id: str, book_id: str):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError("Book not found")

        member = self.members[member_id]
        book = self.books[book_id]
        member.return_book(book)

    def get_borrowed_books(self, member_id: str):
        if member_id not in self.members:
            raise ValueError("Member not found")
        # Restituisce solo i titoli dei libri
        return [book.title for book in self.members[member_id].borrowed_books]
