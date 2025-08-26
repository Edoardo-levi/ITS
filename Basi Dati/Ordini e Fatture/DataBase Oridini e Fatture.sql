-- Creazione di Domini

create domain CodiceFiscale as varchar(16)
	check (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'
);

create type PartitaIVA as varchar(11)
	check (value ~ '^[0-9]{11}$');


create domain Telefono as varchar (16);

create domain Email AS varchar
	check ( value ~ '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
);

create domain Cap as varchar (5)
	check(value ~ '[0-9]{5}');

create type StatoOrdine as
	enum ('In Preparazione', 'Inviato', 'Da Saldare', 'Saldato');

create domain RealTZU as real 
	-- TZU (Tra Zero e Uno)
	check(value >=0 and value <=1);

create domain RealGEZ as real
	check (value >=0);

create type Indirizzo(
	via varchar(100),
	civico integer,
	cap Cap
);
	
create domain IntGEZ as integer
	check(value>=0);

create domain StringaM as varchar(100);



-- Creazione Tabelle

create table Citta (

	nome StringaM not null,

	primary key (nome),

	foreign key (regione) 
		references Regione (nome)

);
create table Regione (

	nome StringaM not null,

	primary key (nome),

	foreign key (nazione)
		references Nazione (nome)

);
create table Nazione (

	nome StringaM not null,

	primary key (nome)

);
create table Direttore (

	nome StringaM not null,
	cognome StringaM not null,
	cf CodiceFiscale not null,
	anni_servizio IntGEZ not null,
	data_nascita date not null,

	primary key (cf),

	foreign key citta
		references Citta (nome)

);
create table Dipartimento (

	nome StringaM not null,
	indirizzo Indirizzo not null,

	primary key (nome),

	foreign key direttore
		references Direttore (cf),

	foreign key citta
		references Citta (nome)
);
create table Fornitore (

	ragione_sociale StringaM not null,
	partita_iva PartitaIVA not null,
	indirizzo Indirizzo not null,
	telefono Telefono not null,
	email Email not null,

	primary key (partita_iva),

	foreign key citta
		references Citta (nome),
	foreign key ordine
		references Ordine (codice)

);
create table Ordine (

	data_stipula Date not null,
	imponibile RealGEZ not null,
	aliquota RealTZU not null,
	descrizione StringaM not null,
	codice IntGEZ not null,

	primary key (codice),

	foreign key dipartimento
		references Dipartimento (nome),
	foreign key statoordine
		references StatoOrdine (nome)

);
create table StatoOrdine (

	nome StringaM not null,

	primary key (nome)

);