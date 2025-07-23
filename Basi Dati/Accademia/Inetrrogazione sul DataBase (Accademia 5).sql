-- 1
select wp, wp.inizio, wp.fine, wp.nome
	from wp, progetto p
		where wp.progetto = p.id
		and p.nome = "Pegasus";

-- 2
select pers.id, pers.nome, pers.cognome, pers.posizione
	from AttivitaProgetto attprog, progetto prog, persona pers
		where attprog.progetto = prog.id 
			and attprog.persona = pers.id
			and prog.nome = "Pegasus";

-- 3 

select pers.id, pers.nome, pers. posizione
	from AttivitaProgetto attprog1,AttivitaProgetto attprog2, progetto prog, persona pers
		where attprog1.id <> attprog2.id
			and attprog1.progetto = attprog2.progetto
			and attprog1.persona  = attprog2.persona
			and attprog1.persona  = persona.id
			and attprog1.progetto = prog.id
			and prog.nome = "Pegasus";


-- 4
select pers.id, pers.nome, pers.cognome, posizione
	from Assenza ass, persona pres
		where ass.persona = pers.id
			and tipo = "Malattia"
			and posizione = "Professore Oridinario";


-- 5
select pers.id, pers.nome, pers.cognome, posizione
	from Assenza ass1, persona pers, Assenza ass2
		where ass1.persona = pers.id
		and ass2.persona = pers.id
		and ass1.id <> ass2.id
		and ass1.tipo = "Malattia"
		and ass2.tipo = "Malattia"
		and pers.posizione = "Professore Oridinario";


-- 6
select pers.id, pers.nome, pers.cognome
	from persona pers, AttivitaNonProgettuale anp
		where pers.id = anp.persona
		and anp.tipo = "Didattica"
		and pers.posizione = "Ricercatore";


-- 7 

select  pers.id, pers.nome, pers.cognome
	from persona pers, attivitanonprogettuale anp1, attivitanonprogettuale anp2
		where anp1.id <> anp2.id
			and anp1.tipo = 'Didattica'
			and anp2.tipo = 'Didattica'
			and anp1.persona = pers.id
			and anp2.persona = pers.id
			and s.posizione = 'Ricercatore';

-- 8
select  pers.id, pers.nome, pers.cognome
	from persona pers, attivitaprogetto attprog, attivitanonprogettuale anp
		where
			pers.id = attprog.persona
			and pers.id = anp.persona
			and attprog.giorno = anp.giorno;


-- 10
select pers.id, pers.nome, pers.cognome
	from persona pers, attivitaprogetto ap, assenza a
		where pers.id = ap.persona
			and a.persona = pers.id
			and ap.giorno = a.giorno;
