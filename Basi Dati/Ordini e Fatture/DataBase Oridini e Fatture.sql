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
	check(value >=0 and value <=1);

create type Indirizzo(
	via varchar(100),
	civico integer,
	cap Cap
);
	
create domain IntGEZ as integer
	check(value>=0)