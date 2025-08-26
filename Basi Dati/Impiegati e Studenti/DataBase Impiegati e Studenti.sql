-- Creazione Domini

create domain CodiceFiscale as varchar (16)
	check (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'
);

create type Ruolo as
	enum ('Segretario', 'direttore', 'Progettista');

create domain RealGEZ as real
	check(value >= 0);

create type Maternita as 
	enum ('0','1');

create type Genere as
	enum ('M', 'F');

create type Responsabile as 
	enum('0', '1');

create domain Stringa as varchar (100);

create domain IntGEZ as integer
	check (value >=0);


-- Creazione tabelle


create table Posizionemilitare (

	nome Stringa not null,

	primary key (nome)

);

create table Persona (

	nome Stringa not null,
	cognome Stringa not null,
	cf CodiceFiscale not null,
	nascita date not null,
	genere Genere not null,
	maternita Maternita not null,

	primary key (cf)

);

create table Studente (

	matricola IntGEZ not null,

	primary key (matricola)

);

create table Impiegato (

	stipendio RealGEZ not null,
	ruolo Ruolo not null,
	is_responsabile Responsabile not null,

	primary key (ruolo)
);

create table Progetto (

	nome Stringa not null,

	primary key (nome)
);