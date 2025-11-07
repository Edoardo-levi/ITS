def check_security_alarm(s1: bool, s2: bool, s3: bool) -> str:
    if (s1==True and(s2 ==False or s3==False) ):
        return "Allarme Attivato"
    else:
        return "Nessun Allarme"
    