"""Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
e aggrega i voti per studente in un nuovo dizionario."""

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
   nuovo_dict:dict[str, list[int]]={}
   for voto in voti:
      nome=voto["nome"]
      voto_preso= voto["voto"]
      if nome in nuovo_dict:
         nuovo_dict[nome].append(voto_preso)
      else:
         nuovo_dict[nome]=[voto_preso]
   return nuovo_dict