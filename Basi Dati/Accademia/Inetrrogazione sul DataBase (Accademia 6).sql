-- 1
	select posizione, count(posizione) as Numero_Strutturato
		from Persona
			group by posizione;


-- 2
	select count(stipendio)
		from persona
			where stipendio>=40000;
				

-- 3
	select count(Progetto)
		from Progetto
			where progetto.fine < CURRENT_DATE and budget > 50000;

-- 4
	select avg (oredurata) as media, min(oredurata) Minimo, max(oredurata) Massimo
		from AttivitaProgetto, Progetto
				where progetto.nome = 'Pegasus' and Progetto.id = AttivitaProgetto.progetto;

-- 5
	select  p.id AS id_persona, p.nome, p.cognome,avg(ap.oreDurata) AS media,min(ap.oreDurata) AS minimo,max(ap.oreDurata) AS massimo
		from Persona p, AttivitaProgetto ap, Progetto pr
			where p.id = ap.persona
  				and ap.progetto = pr.id
  				and pr.nome = 'Pegasus'
					group by p.nome, p.cognome, p.id

-- 6
	select id as id_persona, nome, cognome, sum(oredurata) as ore_didattica
		from persona, AttivitaNonProgettuale
			where persona.id = AttivitaNonProgettuale.persona
				and AttivitaNonProgettuale.tipo= 'Didattica'


-- 7
select avg(stipendio)as media, max(stipendio) as massimo, min(stipendio) as minimo
	from Persona
		where persona.posizione='Ricercatore'

-- 8
select posizione, avg(stipendio) as media, min(stipendio)as minimo, max(stipendio) as massimo
	from  Persona
		where Persona.posizione = 'Professore Ordinario'
			or Persona.posizione='Professore Associato'
			or Persona.posizione='Ricercatore'
		group by Persona.posizione
		

-- 9
	select  Progetto.id as id_progetto, Progetto.nome as progetto, sum(AttivitaProgetto.oredurata) as totale_ore
		from Persona, AttivitaProgetto, Progetto
			where Persona.id = AttivitaProgetto.persona
				  and AttivitaProgetto.progetto = Progetto.id
				  and Persona.nome = 'Ginevra'
				  and Persona.cognome = 'Riva'
			group by Progetto.id, Progetto.nome;
