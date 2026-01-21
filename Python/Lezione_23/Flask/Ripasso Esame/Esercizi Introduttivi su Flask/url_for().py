from flask import Flask, url_for

app = Flask(__name__)

# --- DATI FITTIZI (Mock Data) ---
utenti_db = ["Edoardo", "Andrea", "Francesca", "Max"]
posts_db = {
    1: {"titolo": "Introduzione a Flask", "contenuto": "Flask è un micro-framework potente..."},
    2: {"titolo": "Routing Dinamico", "contenuto": "Imparare url_for è fondamentale..."},
    3: {"titolo": "Template Engines", "contenuto": "Jinja2 permette di creare HTML dinamico..."}
}

# --- HOMEPAGE ---
@app.route('/')
def home():
    return f"""
    <h1>Menu Principale</h1>
    <ul>
        <li><a href="{url_for('lista_utenti')}">Elenco Utenti (Dinamico)</a></li>
        <li><a href="{url_for('lista_posts')}">Blog (Elenco Post)</a></li>
        <li><a href="{url_for('extra')}">Pagina Extra</a></li>
    </ul> 
    """

# --- SEZIONE UTENTI (Navigazione Dinamica) ---

@app.route('/users')
def lista_utenti():
    titolo = "<h1>Scegli un utente:</h1><ul>"
    for nome in utenti_db:
        # Generiamo il link dinamico per ogni utente nel "database"
        link = url_for('scegli_utente', nome=nome)
        titolo += f'<li><a href="{link}">\
            {nome}</a></li>'
    titolo += "</ul><br><a href='/'>Torna alla Home</a>"
    return titolo

@app.route('/users/utenti/<string:nome>')
def scegli_utente(nome: str) -> str:
    return f"<h1>Profilo di {nome}</h1><p>Benvenuto nella pagina dedicata a {nome}!</p>\
        <a href='/users'>Indietro</a>"

# --- SEZIONE BLOG (Mini Blog) ---

@app.route('/posts')
def lista_posts():
    html = "<h1>Articoli del Blog</h1><ul>"
    for post_id, info in posts_db.items():
        # Generiamo il link usando l'ID del post
        link = url_for('mostra_post', id=post_id)
        html += f'<li><a href="{link}">{info["titolo"]}</a></li>'
    html += "</ul><br><a href='/'>Torna alla Home</a>"
    return html

@app.route('/posts/<int:id>')
def mostra_post(id: int):
    post = posts_db.get(id)
    if post:
        return f"""
            <h1>{post['titolo']}</h1>
            <p>{post['contenuto']}</p>
            <hr>
            <a href='/posts'>Torna al Blog</a>
        """
    return "<h1>Errore</h1><p>Post non trovato</p><a href='/posts'>Indietro</a>", 404

# --- ALTRE ROTTE ---

@app.route('/extra')
def extra() -> str:
    return "<h1>Extra Page</h1><p>Questa è la pagina di descrizione.</p><a href='/'>Home</a>"

if __name__ == '__main__':
    app.run(debug=True)
