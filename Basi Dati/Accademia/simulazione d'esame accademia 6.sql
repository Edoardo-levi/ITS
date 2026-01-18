-- 1. Quanti sono gli strutturati di ogni fascia?
	select count(id), posizione
		from persona
			group by (posizione);

-- 2 Quanti sono gli strutturati con stipendio ≥ 40000?
	select count(id)
		from persona
			where persona.stipendio >= 40000;

-- 3 Quanti sono i progetti già finiti che superano il budget di 50000?

	select count(id)
		from progetto
			where fine < now()
			and budget > 50000;

-- 4 Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto
-- ‘Pegasus’?

	select avg(AttivitaProgetto.oreDurata) as media, max(AttivitaProgetto.oredurata) as massimo, min(AttivitaProgetto.oredurata) as minimo
		from AttivitaProgetto, progetto
			where progetto.nome = 'Pegasus'
				and progetto.id = AttivitaProgetto.progetto 
			group by(progetto.nome);

-- 5 Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto
-- ‘Pegasus’ da ogni singolo docente?

	select avg(AttivitaProgetto.oreDurata), max(AttivitaProgetto.oredurata), min(AttivitaProgetto.oredurata),persona.nome, persona.cognome
		from progetto, AttivitaProgetto,persona
			where progetto.nome = 'Pegasus'
				and AttivitaProgetto.progetto = Progetto.id
				and AttivitaProgetto.persona = persona.id
				group by( persona.nome, persona.cognome);


-- 6 Qual è il numero totale di ore dedicate alla didattica da ogni docente?
	
	select persona.id, sum(AttivitaNonProgettuale.oreDurata),persona.nome, persona.cognome
		from  persona, AttivitaNonProgettuale
			where persona.id = AttivitaNonProgettuale.persona
				and AttivitaNonProgettuale.tipo = 'Didattica'
				group by (persona.id);


-- 7  Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

	select max (stipendio) as massimo, min(stipendio) as minimo, avg (stipendio) as media
		from persona
			where persona.posizione = 'Ricercatore'
			group by(persona.posizione);

-- 8 Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori
-- associati e dei professori ordinari?

	select posizione,avg(stipendio)as media, max(stipendio) as massimo, min(stipendio) as minimo
		from persona
			group by (persona.posizione);

-- 9 Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

	select persona.id, persona.nome, persona.cognome,progetto.nome, sum(AttivitaProgetto.oreDurata)
		from persona, AttivitaProgetto, progetto
			where persona.nome = 'Ginevra'
				and persona.cognome ='Riva'
				and persona.id = AttivitaProgetto.persona
				and AttivitaProgetto.progetto= progetto.id
				group by(persona.nome,persona.cognome,progetto.nome,persona.id);
 