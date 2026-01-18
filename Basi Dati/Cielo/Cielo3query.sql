-- 1 Qual è la durata media, per ogni compagnia, dei voli che partono da un aeroporto
-- situato in Italia?

select avg(volo.durataMinuti), LuogoAeroporto.nazione,Arrpart.partenza, Arrpart.comp
	from Arrpart, volo, LuogoAeroporto
		where LuogoAeroporto.nazione ='Italy'
			and LuogoAeroporto.aeroporto =Arrpart.partenza
			and volo.codice = Arrpart.codice
		group by (LuogoAeroporto.nazione,Arrpart.partenza, Arrpart.comp);



-- 2 Quali sono le compagnie che operano voli con durata media maggiore della durata
-- media di tutti i voli?

	select avg(volo.durataMinuti),
		from volo,