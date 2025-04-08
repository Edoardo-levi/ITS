def caratteristiche_auto(produttore: str, modello: str, **kwargs):
    auto: dict = {"produttore": produttore, "modello": modello}
    auto.update(kwargs)
    return auto