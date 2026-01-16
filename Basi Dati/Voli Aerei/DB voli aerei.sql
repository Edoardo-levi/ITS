-- creazione domini e tabelle
create domain IntMDZ as integer
	check (value>0);

create domani IntMN as integer
	check (value > 1900)

create domain Codice as char(20) 
	check(~ '^([A-Z0-9]{2}|[A-Z]{3})\s?[0-9]{1,4}[A-Z]?$');

create domani IntMUZ as integer
	check (value >= 0);


-- Creazione tabelle

create table Volo (
	codice varchar(100) not null,
	durata_min IntMDZ not null,
	codice_volo Codice primary key,
	foreign key (aeroporto)
		references aeroporto (codice_areoporto)
);


create table Compagnia (
	nome varchar(100) not null,
	anno IntMN not null,
	codice_compagnia Codice primary key,
	foreign key (citta)
		references citta (nome)
);

create table Nazione (
	nome varchar (100)
);

create table Aeroporto (
	codice varchar(100) not null,
	nome varchar(100) not null,
	codice_areoporto Codice primary key
	foreign key (citta)
		references citta (nome)
);