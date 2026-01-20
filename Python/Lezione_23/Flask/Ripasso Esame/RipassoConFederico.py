class Persona():
    def __init__(self, id:str, nome: str, cognome: str, capelli: bool):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.capelli = capelli

    def info(self):
        return {"id":self.id,"nome":self.nome, "cognome":self.cognome, "capelli":self.capelli}

l_persone: list[Persona] = []
l_persone.append(Persona("p1", "Rob", "Del", False))
l_persone.append(Persona("p2", "Mattia", "Diggio", True))
l_persone.append(Persona("p3", "Mauro", "Murgia", False))
l_persone.append(Persona("p4", "Play", "Dido", False))


from flask import Flask, url_for, jsonify, request

app = Flask(__name__)


#get per le persone
@app.route("/persone", methods=["GET"])
def persone():
    return jsonify([persona.info() for persona in l_persone])

#post per creare nuova persona
@app.route("/add_persona", methods=["POST"])
def add_persona():
    data = request.get_json()

    for persona in l_persone:
        if persona.id == data["id"]:
            return jsonify({"errore":"id già presente"})
        
    new_persona = Persona(data["id"], data["nome"], data["cognome"], data["capelli"])
    l_persone.append(new_persona)
    return jsonify({"messaggio":"persona aggiunta con successa gg ggg gg gg"})

@app.route("/del_persona/<string:id_persona>", methods=["DELETE"])
def del_persona(id_persona):
    for persona in l_persone:
        if persona.id == id_persona:
            l_persone.remove(persona)
            return jsonify({"messaggio":"persona eliminata con successa"})
    return jsonify({"errore":"id persona non presente"})

    

#route statica
@app.route("/ciao")
def ciao():
    return f"<h1>CIAOCIAOCIAOCIAO</h1>"

#route dinamica
@app.route("/users/<string:user_id>")
def users(user_id):
    return f"<h1>Ciao questo e' il profilo di {user_id}</h1>"

@app.route("/somma/<int:x>/<int:y>")
def somma(x, y):
    return f"<h1>La somma tra {x} e {y} è {x+y}</h1>"

# i tipi per i parametri delle route dinamiche, string, float, int e bool

@app.route("/")
def home():
    return f'''<h1>Questa è la home</h1>
    {url_for("ciao")}
    <br>
    {url_for("somma", x=5, y=7)}
    <br>
    <a href="{url_for("users", user_id="peppe")}">VAI AL PROFILO DI PEPPE</a>'''

if __name__ == "__main__":
    app.run(debug=True)