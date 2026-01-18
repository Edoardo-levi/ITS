-- creazione domini e tipi 

create domain IntGZ as 
	integer check(value >0);

create type  Posizione as 
	enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type  Assenza as
	enum ('Chiusura Universitaria', 'Maternita', 'Malattia');

create type istituzionale as
	enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro
Accademico', 'Altro');

create type progettuale as
	enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');


-- creazione database

create table Nazione (
	nome varchar(100) primary key

);
create table Regione (
	nome varchar(100) primary key,
	nazione varchar(100) not null,
	unique (nome, nazione),
	foreign key (nazione) 
		references nazione (nome)
);

create table citta(
	nome varchar(100)primary key,
	regione varchar(100) not null,
	unique (nome, regione),
	foreign key(regione)
		references regione (nome)
);


create table Docente_Universitario (
	nome varchar(100) not null,
	cognome varchar(100) not null,
	data_di_nascita date not null,
	matricola IntGZ primary key,
	posizione Posizione not null,
	citta varchar(100),
	foreign key (citta)
		references citta(nome)
);

create table Progetto_di_Ricerca (
	nome varchar(100) not null,
	acronimo varchar(100) primary key,
	data_inizio date not null,
	data_fine date,
	Docente_Universitario IntGZ,
	foreign key (Docente_Universitario)
		references Docente_Universitario (matricola)

);

create table Impegno_docente (
	giorno date not null,
	dureata_ore IntGZ not null,
	id integer primary key,
	Docente_Universitario IntGZ,
	foreign key (Docente_Universitario)
		references Docente_Universitario (matricola)
);

create table Work_Package (
	nome varchar(100) not null,
	inizio date not null,
	fine date,
	id integer primary key,
	Progetto_di_Ricerca varchar not null,
	foreign key (Progetto_di_Ricerca)
		references Progetto_di_Ricerca (acronimo)
);

create table Assenza (
	assenza Assenza not null,
	Impegno_docente integer not null,
	primary key (Impegno_docente),
	foreign key (Impegno_docente) 
		references Impegno_docente (id)
);

create table Impegno_docente(
	progettuale progettuale not null,
	Impegno_docente integer primary key,
	foreign key (Impegno_docente)
		references Impegno_docente (id)
);

create table Impegno_docente (
	istituzionale istituzionale not null,
	Impegno_docente integer primary key,
	foreign key (Impegno_docente)
		references Impegno_docente (id)
);

