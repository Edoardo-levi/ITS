-- Creazionie tipi e domini
create domain IntGEZ as integer 
    check (value >= 0);

create domain Stringa as varchar(300);

create domain Voto as integer 
    check (
    value >= 1
    and value <= 5
);

create domain RealGZ as real 
    check (value >= 0);


create domain RealMGZ as real
    check (value>0);

create type Condizione as 
    enum ('Nuovo', 'Usato');

