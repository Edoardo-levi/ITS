-- creazione domini

create domain RealGEZ as 
	real default 0 check(value>=0);

create domain RealGZ as
	real default 0 check (value > 0);


-- creazione tabelle 
create table Nazione (
	id integer primary key
);

create table Regione (
	id integer primary key,
	nazione integer not null,
	foreign key(nazione)
		references nazione (id),
	unique (id,nazione)
);

create table Citta (
	id integer primary key,
	regione integer not null,
	foreign key (regione)
		references regione (id),
	unique (regione,id)
);

create table Artista (
	nome_arte varchar(100) not null,
	data_nascita date not null,
	data_mote date,
	id integer primary key,
	citta integer not null,
	foreign key (citta)
		references citta(id)
);


create table Tecnica (
	nome varchar(100) not null,
	id integer primary key
);

create table Categoria (
	nome varchar(100) primary key
);

create table CorrenteArtistica (
	nome varchar(100) primary key
);

create table Opera (
	nome varchar(100) not null,
	anno_realizzazione integer not null,
	id integer primary key,

	artista integer not null,
	foreign key (artista)
		references artista (id),

	tecnica integer not null,
	foreign key (tecnica)
		references tecnica (id),

	categoria varchar(100) not null,
	foreign key (categoria)
		references categoria (nome),

	CorrenteArtistica varchar(100) not null,
	foreign key (CorrenteArtistica)
		references CorrenteArtistica (nome)
);

create table Esposizione (
	nome varchar (100) not null,
	inizio date not null,
	id integer primary key
);

create table Espone (
	inizio date not null,
	fine date,
	id integer primary key,
	Opera varchar(100) primary key,
	Esposizione integer primary key,
	foreign key (opera) 
		references opera (id),

	foreign key (Esposizione)
		references Esposizione (id)
);


create table Permanente (
	esposizione integer primary key,
	foreign key (Esposizione)
		references esposizione(id)
);

create table Temporanea (
	fine date not null,
	tema varchar(100),
	prezzo_accesso RealGZ not null,
	esposizione integer primary key,
	foreign key(esposizione)
		references esposizione (id)
);


create table Tariffa (
	nome varchar (100) primary key,
	prezzo_base RealGEZ not null
);

create table Biglietto (
	istante_vendita: timestamp not null,
	vendita date not null,
	id integer primary key,
	tariffa varchar(100) not null,
	foreign key (tariffa)
		references tariffa (nome)
);

create table Standard (
	biglietto integer primary key,
	foreign	key(biglietto)
		references biglietto (id)
);

create table ExtendedAccess (
	biglietto integer primary key,
	Temporanea integer not null,
	foreign key (biglietto),
		references biglietto (id),
	foreign key (Temporanea)
		references Temporanea(esposizione)
);