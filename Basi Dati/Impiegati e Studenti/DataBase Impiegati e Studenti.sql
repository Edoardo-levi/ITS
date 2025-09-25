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
	pos_mil_nome Stringa, -- FK verso PosizioneMilitare
	primary key (cf),
	foreign key (pos_mil_nome) references Posizionemilitare(nome)
);

create table Studente (
	matricola IntGEZ not null,
	cf CodiceFiscale not null unique, -- FK verso Persona
	primary key (matricola),
	foreign key (cf) references Persona(cf)
);

create table Impiegato (
	stipendio RealGEZ not null,
	ruolo Ruolo not null,
	is_responsabile Responsabile not null,
	cf CodiceFiscale not null unique, -- FK verso Persona
	primary key (cf),
	foreign key (cf) references Persona(cf)
);

create table Progetto (
	nome Stringa not null,
	cf_impiegato CodiceFiscale, -- FK verso Impiegato (responsabile progetto)
	primary key (nome),
	foreign key (cf_impiegato) references Impiegato(cf)