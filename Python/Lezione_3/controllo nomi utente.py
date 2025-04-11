current_users=["Diablo365","Commodor64", "CiccioGamer89","Lupacchiotto", "Ludopatico777"]
new_users= ["LoStirato","St3pny","GinoBuonVino","Ludopatico777","Anima"]


for y in range (len(new_users)):
    if new_users[y] in current_users:
        print(f"ci dispiace ma il nome utente {new_users[y]} e' gia' stato utilizzato nella lista current_users {current_users}")