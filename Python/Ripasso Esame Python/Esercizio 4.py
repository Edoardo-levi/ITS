"""Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.
    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
   
     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    
    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
   
     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    
    - list_recipes(): Elenca tutte le ricette esistenti.
    
    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    
    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente."""


class RecipeManager:
    def __init__(self):
        self.recipes:dict={}
    
    def create_recipe(self,name,ingredients):
        if name in self.recipes:
            return "Errore! La ricetta esiste già'"
        else:
            self.recipes[name]=ingredients
            return {name:self.recipes[name]}

    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return "Errore! La ricetta non esiste"
        elif ingredient  in self.recipes[recipe_name]:
            return "Errore! L'ingrediente esiste già"
        else:
            self.recipes[recipe_name].append(ingredient)
        return {recipe_name:self.recipes[recipe_name]}
    
    def remove_ingredient(self,recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return "Errore! La ricetta non esiste"
        if ingredient not in self.recipes[recipe_name]:
            return "Errore! L'ingrediente non esiste"
        self.recipes[recipe_name].remove(ingredient)
        return {recipe_name: self.recipes[recipe_name]}

    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name not in self.recipes:
            return "Errore! La ricetta non esiste"
        if old_ingredient not in self.recipes[recipe_name]:
            return "Errore! L'ingrediente non esiste"
        nuova_lista = []
        for ingrediente in self.recipes[recipe_name]:
            if ingrediente == old_ingredient:
                nuova_lista.append(new_ingredient)
            else:
                nuova_lista.append(ingrediente)
        self.recipes[recipe_name] = nuova_lista
        return {recipe_name: self.recipes[recipe_name]}

    def list_recipes(self):
        lista:list=[]
        for recipe in self.recipes.keys():
            lista.append(recipe)
        return lista
    
    def list_ingredients(self,recipe_name):
        if recipe_name not in self.recipes:
            return "Errore! La ricetta non esiste"
        else:
            return self.recipes[recipe_name]
    
    def search_recipe_by_ingredient(self,ingredient):
        ricette_trovate={}
        for ricetta, ingredienti in self.recipes.items():
            if ingredient in ingredient:
                ricette_trovate[ricetta]=ingredienti
            else:
                return f"Ricetta non trovata con l'ingrediente: {ingredient}"
        return ricette_trovate