"""Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere,
ritorni un nuovo insieme senza i numeri specificati nella lista."""

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
   new_set =original_set.copy()
   for element in elements_to_remove:
      if element in new_set:
        new_set.remove(element)
   return new_set