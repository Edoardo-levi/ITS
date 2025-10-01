-- creazione tabelle


create table Utente (
    username Stringa primary key,
    registrazione date not null
    );

create table PostOggetto (
    codice IntGEZ primary key,
    descrizione Stringa not null,
    pubblicazione datetime not null,
    ha_feedback boolean not null,
    voto Voto,
    commento Stringa,
    check (
            (ha_feedback = true
                and commento is not null)
        or (ha_feedback = false
                and commento is null)
        ),
        istante_feedback timestamp,
        check (
            (ha_feedback = true
                and istante_feedback is not null
                and istante_feedback > pubblicazione)
            or (ha_feedback = false
                and istante_feedback is null)
        ),
        utente Stringa not null,
        foreign key (utente) references Utente (username),
        tipo char not null check (tipo="Asta" or tipo="CompraloSubito")
    );


create table PostOggettoAsta(
    codice IntGEZ primary key,
    foreign key (codice) references PostOggetto(codice),
    prezzo_base RealGZ not null,
    prezzo_bid RealGZ not null,
    scadenza datetime not null
);

create table PostOggettoCompraloSubito(
    codice IntGEZ primary key,
    foreign key (codice) references PostOggetto(codice),
    prezzo RealGZ not null

);

create table Bid (
    
    istante date not null,
    primary key (istante),
    foreign key (utente) references Utente(username),
    foreign key (codice) references PostOggettoAsta(codice)
);

create table Categoria (
    nome Stringa primary key
    
);

create table MetodoDiPagamento (
    nome Stringa primary key
);

create table VenditoreProf (
    vetrina Stringa primary key
    foreign key (username) references Utente(username),
   
);

create table Privato (
    username Stringa primary key,
    foreign key (username) references Utente(username)
);

create table PostOggettoNuovo (
    anni_garanzia IntGEZ not null,
    foreign key (descrizione) references PostOggetto(descrizione),
    foreign key(vetrina) references VenditoreProf (vetrina)
    
);

create table PostOggettoUsato (
    anni_garanzia IntGEZ not null,
    foreign key (anni_garanzia) references PostOggetto(anni_garanzia)
    
);

