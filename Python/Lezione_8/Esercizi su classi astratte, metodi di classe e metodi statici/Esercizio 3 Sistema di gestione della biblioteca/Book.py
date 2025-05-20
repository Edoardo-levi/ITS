"""Crea una classe Book contenente i seguenti attributi: titolo, autore, ISBN. La classe Book deve contenere i seguenti metodi:

__str__ , metodo per restituire una rappresentazione stringa del libro.

from_string , un metodo di classe per creare un'istanza di Book da una stringa nel formato "titolo, autore, isbn". Significa che è necessario utilizzare il riferimento di classe cls per creare un nuovo oggetto della classe Book utilizzando una stringa.

"""

from typing import Self
class Book:
    def __init__(self, titolo:str, autore:str, isbn:str):
        self.titolo=titolo
        self.autore= autore
        self.isbn= isbn

    def __str__(self) ->str:
        return f"Titolo: {self.titolo}; Autore: {self.autore}; Isbn: {self.isbn}"
    
    @classmethod

    def from_string (cls,repr_str:str) -> Self:
        sub_str=repr_str.split(',')
        return cls(sub_str[0], sub_str[1], sub_str[2])