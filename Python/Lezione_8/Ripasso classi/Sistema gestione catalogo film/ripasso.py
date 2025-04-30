"""Sistema di Gestione Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi della classe:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo."""


class MovieCatalog:

    def __init__(self) ->None:
        self.catalog:dict[str, list[str]]={}

    def add_movie(self, director_name:str, movies:list[str]) ->None:
        if director_name not in self.catalog:
            self.catalog[director_name] = movies
        
        else:
            for movie in movies:
                if movie not in self.catalog[director_name]:
                    self.catalog[director_name].append(movie)
                    
    def remove_movie(self, director_name:str, movie_name:str):
        if director_name in self.catalog and movie_name in self.catalog[director_name]:
            self.catalog[director_name].remove(movie_name)
            if  not self.catalog[director_name]:
                del self.catalog[director_name]
    
    def list_directors(self) ->list[str]:
        return list(self.catalog.keys())

    def get_movies_by_director(self, director_name:str) ->list[str]:
        if director_name in self.catalog:
            return self.catalog[director_name]
        

    def search_movies_by_title(self, title:str) -> dict[str,list[str]] | str:
        
        result:dict[str,list[str]]= {}

        for director, movies in self.catalog.items():
            matching_movies:list[str]=[]
            for movie in movies:
                if movie.lower()==title.lower():
                    matching_movies.append(movie)

            if matching_movies:
                result[director]=matching_movies
        if result:
            return result
        else:
            return "Nessun film trovato"
        




