-- creazione domini e tabelle
create domain IntMDZ as integer
	check (value>0);

create domani IntMN as integer
	check (value > 1900)

create domain Codice as char(20) 
	check(~ '^([A-Z0-9]{2}|[A-Z]{3})\s?[0-9]{1,4}[A-Z]?$');

create domani IntMUZ as integer
	check (value >= 0);


-- creazione tabelle 
create table nazione (
	nome varchar (100) not null,
	id integer not null primary key
);

create table citta (
	nome varchar(100) not null,
	abitanti IntMUZ not null,
	id integer not null primary key,
	nazione integer,
		foreign key (nazione)
			references nazione (id)
);

create table compagnia (
	nome varchar (100) not null,
	anno IntMN not null,
	codice_compagnia Codice primary key
);