 -- 1 Elencare tutti i progetti la cui fine è successiva al 2023-12-31
 select *
	from Progetto where fine > '2023-12-31';

-- 2 Contare il numero totale di persone per ciascuna posizione
-- (Ricercatore, Professore Associato, Professore Ordinario)
select posizione, count(id) as numero_persone
	from Persona
		group by posizione;

-- 3 Restituire gli id e i nomi delle persone che hanno almeno un giorno di assenza per "Malattia"
select persona.id, persona.nome, tipo
	from persona
		join assenza
			on persona.id =assenza.persona
	where tipo= 'Malattia';
	


-- 4 Per ogni tipo di assenza, restituire il numero complessivo di occorrenze
select tipo, count (tipo) as tipo_malattia
	from  assenza
		group by tipo;

-- 5 Calcolare lo stipendio massimo tra tutti i "Professori Ordinari"
select max(stipendio) as stipendio_massimo
	from Persona
		where posizione ='Professore Ordinario';

-- 6 Quali sono le attività e le ore spese dalla persona con id 1
-- nelle attività del progetto con id 4, ordinate in ordine
-- decrescente. Per ogni attività, restituire l’id, il tipo e il
-- numero di ore
select  p.nome, p.cognome, p.id as id_persona, ap.id as id_progetto, tipo, oredurata
	from Persona as p, AttivitaProgetto as ap
	where p.id= 1
	AND ap.progetto = 4
	and p.id = ap.persona

-- 7 Quanti sono i giorni di assenza per tipo e per persona. Per
-- ogni persona e tipo di assenza, restituire nome, cognome,
-- tipo assenza e giorni totali
select p.nome, p.cognome, ass.tipo, COUNT(ass.giorno) as giorni_totali_assenza
	from Persona as p, Assenza as ass
	where p.id = ass.persona
	group by p.nome, p.cognome, ass.tipo
		order by p.cognome, p.nome, ass.tipo;

-- 8 Restituire tutti i “Professori Ordinari” che hanno lo
-- stipendio massimo. Per ognuno, restituire id, nome e
-- cognome
select id, nome,cognome, stipendio as stipendio_max, posizione
	from persona
		where posizione = 'Professore Ordinario'
		and stipendio = (select max(stipendio)
		from persona
		where posizione= 'Professore Ordinario')