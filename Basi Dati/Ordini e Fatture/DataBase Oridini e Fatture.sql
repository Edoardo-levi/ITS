create domain CodiceFiscale as char(16) check (value ~ '^[A-Z0-9]{16}$');

create domain PartitaIva as char(11) check (value ~ '^[0-9]{11}$');

create domain IntGEZ as integer check (value >= 0);

create domain RealGEZ as numeric check (value >= 0);

create domain RealBzo as numeric check (
    value >= 0
    and value <= 1
);

create domain Cap as char(5) check (value ~ '^[0-9]{5}(-[0-9]{4})?$');

create domain stringa as varchar;

create type Indirizzo as (
    via stringa,
    civico IntGEZ,
    cap Cap
);


create type statoOrdine as enum(
    'Da saldare',
    'Saldato',
    'In preparazione',
    'Inviato'
);

create domain Telefono as varchar (10);

create domain Email as varchar check
    (value ~ '^[A-Za-z0-9._%\-+!#$&/=?^|~]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');



create table nazione (
    nome stringa primary key
);

create table regione (
    nome stringa not null,
    nazione stringa not null,
    primary key (nome, nazione),
    foreign key (nazione) references nazione(nome)
);

create table citta (
    id serial primary key, -- serial indica una colonna di valori che genera automaticamente valori unici,
                           -- incrementa un valore per ogni riga nella tabella
    nome stringa not null,
    regione stringa not null,
    nazione stringa not null,
    unique (nome, regione, nazione),
    foreign key (regione, nazione) references regione(nome, nazione)
);

create table direttore (
    nome stringa not null,
    congome stringa not null, 
    cf CodiceFiscale primary key,
    servizio IntGEZ not null, 
    nascita date not null,
    citta IntGEZ not null,
    foreign key (citta) references citta(id)
);

create table dipartimento (
    nome stringa primary key,
    indirizzo indirizzo not null,
    citta IntGEZ not null,
    foreign key (citta) references citta(id),
    direttore CodiceFiscale not null,
    foreign key (direttore) references direttore(cf)
);

create table fornitore (
    nome stringa not null,
    iva PartitaIva primary key,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email Email not null,
    citta IntGEZ not null,
    foreign key(citta) references citta(id)
);

create table stati (
    stato stringa primary key
);

create table ordine (
    codice IntGEZ primary key,
    data_stipula date not null,
    imponibile RealGEZ not null,
    aliquota RealBzo not null,
    descrizione stringa not null,
    dipartimento stringa not null,
    foreign key (dipartimento) references dipartimento(nome),
    stato stringa not null,
    foreign key (stato) references stati (stato),
    fornitore PartitaIva not null,
    foreign key (fornitore) references fornitore(iva)
);


select extract ('year' from age(current_date, nascita)) from direttore where direttore.cf="ecc";
-- con questa riga di codice, ottengo gli anni dei direttori con cf = "ecc"