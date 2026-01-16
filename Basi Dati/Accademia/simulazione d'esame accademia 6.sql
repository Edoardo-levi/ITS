-- 1. Quanti sono gli strutturati di ogni fascia?
	select persona.posizione,  count(persona.id) 
		from persona 
			group by (persona.posizione);

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?
	select count(persona.id)
		from persona
			where persona.stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?
	select count(progetto.id)
		from progetto
			where progetto.fine < now()
				and progetto.budget > 50000;

-- 4 Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto 
-- ‘Pegasus’?
	select progetto.nome, avg(attivitaprogetto.oredurata) as media, max(attivitaprogetto.oredurata) as massimo, min(attivitaprogetto.oredurata)
		from progetto, attivitaprogetto
			where progetto.nome = 'Pegasus'
			and progetto.id= attivitaprogetto.progetto
			group by (progetto.nome);

-- 5 Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?
	select  persona.nome, persona.cognome, avg(attivitaprogetto.oredurata), min(attivitaprogetto.oredurata), max(attivitaprogetto.oredurata)
		from progetto, attivitaprogetto, persona
			where progetto.nome = 'Pegasus'
			and progetto.id= attivitaprogetto.progetto
			and attivitaprogetto.persona = persona.id
		group by (persona.nome, persona.cognome);