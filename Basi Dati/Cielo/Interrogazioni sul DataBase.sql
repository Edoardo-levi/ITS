-- 1 Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
select Volo.codice, Compagnia.nome
from Volo, Compagnia
where volo.comp= Compagnia.nome
and Volo.durataMinuti>180

-- 2 Quali sono le compagnie che hanno voli che superano le 3 ore?
select distinct Compagnia.nome
from Compagnia, Volo
where Volo.comp = Compagnia.nome
and Volo.durataMinuti > 180

-- 3 Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con
-- codice ‘CIA’?
select Volo.codice, Compagnia.nome
from Volo, Compagnia, ArrPart
where Volo.codice = Arrpart.codice
and Volo.comp = Compagnia.nome
and ArrPart.partenza = 'CIA'

-- 4 Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice
-- ‘FCO’?
select distinct Compagnia.nome
from Compagnia, Volo, ArrPart
where Volo.comp = Compagnia.nome
and Volo.codice = ArrPart.codice
and ArrPart.arrivo = 'FCO'

--  5 Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’
-- e arrivano all’aeroporto ‘JFK’?
select Volo.codice, Compagnia.nome
from Volo, Compagnia, ArrPart
where Volo.codice = ArrPart.codice
and Volo.comp = Compagnia.nome 
and ArrPart.partenza = 'FCO'
and ArrPart.arrivo = 'JFK'

-- 6 Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’?
select Compagnia.nome
from Volo, ArrPart, Compagnia
where Volo.codice= ArrPart.codice 
and Volo.comp = Compagnia.nome
and ArrPart.partenza = 'FCO'
and ArrPart.arrivo = 'JFK'

-- 7 Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla
-- città di ‘New York’?
select distinct Compagnia.nome
from Volo, Compagnia, ArrPart, LuogoAeroporto partenza, LuogoAeroporto arrivo
where Volo.comp = Compagnia.nome
and Volo.codice = ArrPart.codice
and ArrPart.partenza = partenza.aeroporto
and ArrPart.arrivo = arrivo.aeroporto
and partenza.citta = 'Roma'
and arrivo.citta = 'New York'

-- 8 Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli
-- della compagnia di nome ‘MagicFly’?
select Aeroporto.codice codice_IATA, Aeroporto.nome, LuogoAeroporto.citta, LuogoAeroporto.nazione
from Aeroporto, LuogoAeroporto, ArrPart, Volo
where Aeroporto.codice = LuogoAeroporto.aeroporto
and Aeroporto.codice = ArrPart.partenza
and ArrPart.codice = Volo.codice 
and Volo.comp= 'MagicFly'

-- 9 Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e
-- atterrano ad un qualunque aeroporto della città di ‘New York’? Restituire: codice
-- del volo, nome della compagnia, e aeroporti di partenza e arrivo.
select  Volo.codice,   Compagnia.nome, ArrPart.arrivo, Arrpart.partenza 
from Volo, Compagnia, Arrpart, LuogoAeroporto partenza, LuogoAeroporto arrivo
where volo.comp = Compagnia.nome
and VOlo.codice = ArrPart.codice
and ArrPart.arrivo = arrivo.aeroporto
and ArrPart.partenza = partenza.aeroporto
and partenza.citta = 'Roma'
and arrivo.citta = 'New York'

-- 11 Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?
select distinct Compagnia.nome Compagnia, Compagnia.annoFondaz anno_fondazione
from Compagnia, Volo, ArrPart
where Volo.comp = Compagnia.nome
and Volo.codice = ArrPart.codice
and ArrPart.partenza = 'FCO'
and ArrPart.arrivo = 'JFK'
and Compagnia.annoFondaz is not null