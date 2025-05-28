from mytipes import NumeroTelefono, Indirizzo
class Dipartimento:

    _nome: str # noto alla nascita
    _telefoni: set[NumeroTelefono] # [1..*] noto alla nascita
    _indirizzo: Indirizzo | None  # [0..1] possibilmente non noto alla nascita

    def __init__(self, nome: str, tel: NumeroTelefono, ind: Indirizzo|None) -> None:
        self.set_nome(nome)

        # opzione 1
        self._telefoni = set()
        self.add_NumeroTelefono(tel)
        # opzione 2
        # self.set_telefoni({tel})

        self.set_indirizzo(ind)

    def nome(self) -> str:
        return self._nome

    def indirizzo(self) -> Indirizzo | None:
        return self._indirizzo

    def telefoni(self) -> frozenset[NumeroTelefono]:
        return frozenset(self._telefoni)

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_indirizzo(self, i: Indirizzo | None) -> None:
        self._indirizzo = i

    def add_NumeroTelefono(self, NumeroTelefono: NumeroTelefono) -> None:
        self._telefoni.add(NumeroTelefono)

    def set_telefoni(self, telefoni: set[NumeroTelefono]) -> None:
        if not telefoni: # equivalente a len(telefoni) == 0
            raise ValueError("Il dipartimento deve avere almeno un NumeroTelefonoro di NumeroTelefono")
        self._telefoni = telefoni

    def remove_NumeroTelefono(self, NumeroTelefono: NumeroTelefono) -> None:
        if len(self._telefoni) >= 2: # NumeroTelefono è [1..*]!
            self._telefoni.remove(NumeroTelefono)
        else:
            raise RuntimeError("Il dipartimento deve avere almeno un NumeroTelefonoro di NumeroTelefono")

    def __str__(self):
        if self._indirizzo is None:
            ind_str: str = "senza sede"
        else:
            ind_str: str = f"con sede in {self.indirizzo()}"

        return f"Dipartimento '{self.nome()}' {ind_str} e NumeroTelefonori NumeroTelefono: {self.telefoni()}"


if __name__ == "__main__":
    pass