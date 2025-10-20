-- 1
select a.codice as codice_aeroporto,a.nome as aeroporto,count(distinct v.comp) as num_compagnie
    from aeroporto a, arrpart ap, volo v
      where v.comp = ap.comp
        and (ap.arrivo = a.codice or ap.partenza = a.codice)
group by a.codice, a.nome;

-- 2
  select count(Volo) as num_voli
      from ArrPart, Volo
        where ArrPart.partenza = 'HTR'
          and Volo.durataMinuti >=100
          and Volo.comp = ArrPart.comp
          and Volo.codice = ArrPart.codice
-- 3
select la.nazione, count(distinct a.codice) as num_aerop
    from aeroporto a, luogoaeroporto la, arrpart ap
      where ap.comp = 'apitalia'
        and (ap.arrivo = a.codice or ap.partenza = a.codice)
        and a.codice = la.aeroporto
group by la.nazione;


-- 4
select  avg(v.durataMinuti) as media, min(v.durataMinuti) as minimo, max(v.durataMinuti) as massimo
      from volo v
where v.comp = 'magicfly';


-- 5
select a.codice as codice_aeroporto, a.nome as aeroporto, min(c.annoFondaz) as anno
    from aeroporto a, arrpart ap, compagnia c
        where ap.arrivo = a.codice 
        or ap.partenza = a.codice
        and ap.comp = c.nome
group by a.codice, a.nome;

-- 6
select la1.nazione as partenza, count(distinct la2.nazione) as raggiungibili
  from luogoaeroporto la1, luogoaeroporto la2, arrpart ap
    where ap.partenza = la1.aeroporto
      and ap.arrivo = la2.aeroporto
group by la1.nazione;

-- 7 
select ap.partenza as codic,a.nome as aeroporto,avg(v.durataMinuti) as media_durata
  from arrpart ap, volo v, aeroporto a
    where v.codice = ap.codice
      and v.comp = ap.comp
      and ap.partenza = a.codice
group by ap.partenza, a.nome;


-- 8
select c.nome, sum(v.durataMinuti) as durata_tot
    from compagnia c, volo v
      where v.comp = c.nome
        and c.annoFondaz >= 1950
group by c.nome;

