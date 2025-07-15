-- 1

select distinct cognome
from Persona;


-- 2

select id, nome, cognome
from Persona
where posizione = 'Ricercatore';

-- 3

select id, nome, cognome
from Persona
where posizione = 'Professore Associato'
  and cognome like 'V%';


-- 4

select id, nome, cognome
from Persona
where posizione in ('Professore Associato', 'Professore Ordinario')
  -- L'operatore 'in' può essere usato per decidere se il valore dell'attributo
  -- 'posizione' è tra quelli di una lista ordinata di valori separati da virgole.
  -- Vedremo altri usi dell'operatore 'in' più avanti.
  and cognome like 'V%';


-- 5

select *
from Progetto
where fine < CURRENT_DATE;


-- 6 
select id, nome
from Progetto
order by inizio asc;


-- 7
select id, nome
from WP
order by nome asc;


-- 8

select distinct tipo
from Assenza;


-- 9
select distinct tipo
from AttivitaProgetto;


-- 10
select distinct giorno
from AttivitaNonProgettuale
where tipo = 'Didattica'
order by giorno;