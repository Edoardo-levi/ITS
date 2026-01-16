-- creazione domini
create domain intgez as integer
	check (value>=0);

-- creazione tabelle 

create table Falesia (
	nome varchar (100) primary key
);

create table grado (
	nome varchar (100) primary key,
	valore intgez not null,

);



create table utente (
	username varchar(100) primary key
);

create table chiodatore (
	utente varchar(100) primary key,
	foreign key (utente) references utente (username),
	x varchar(100) not null,
	unique (x) -- {id2} nel diagramma
);

create table arrampicatore (
	utente varchar(100) primary key,
	foreign key (utente) references utente (username),
	nome varchar(100), -- opzionale quindi non metto not null
	cognome varchar (100) -- opzionale quindi non metto not null 	
);

crate table via (
	nome varchar(100) not null,
	n intgez not null,
	falesia varchar(100) not null,
	foreign key (falesia)
		references falesia(nome),  	-- associazione verso falesia
	primary key(nome, falesia),
	grado varchar(100) not null, 
		foreign key (grado)
			references grado (nome) -- associazione verso grado 
	-- vincolo di includione (nome, falesia) occorre in crea(nome_via, falesia)

);

create table crea (
	nome_via varchar(100) not null,
	falesia varchar(100) not null,
	foreign key (nome_via,falesia) references via (nome,falesia)
	chiodatore varchar not null,
	foreign key (chiodatore) references chiodatore (utente)
	primary key (nome_via, falesia, chiodatore)
);

create table sallita (
	id integer primary key,
	data date not null,
	nome_via varchar(100) not null,
	falesia varchar(100) not null,
	foreign key(nome_via falesia)
		references via (nome,falesia),
		arrampicatore varchar(100) not null,
		foreign key (arrampicatore) 
			references arrampicatore(utente)

);