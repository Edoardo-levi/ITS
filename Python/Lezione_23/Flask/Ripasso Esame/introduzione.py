from flask import Flask, url_for

app = Flask (__name__)


@app.route('/')
def home ()-> str:
    return f"<h1> Ciao mi chiamo Edoardo</h1>"

@app.route('/users/<string:username>')
def show_user_profile(username:str)-> str:
    return f"<h2>profilo di {username}</h2>"

@app.route('/users/<int:post_id>')
def show_post_id(post_id:int) -> int:
    return f"<h2>post {post_id}</h2>"


with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='edoardo'))
    print(url_for('show_post_id', post_id=42))

"""La funzione url_for() ti permette di ricostruire l'URL (cioè la rotta) per una funzione specifica. È utile perché:

Ti permette di far costruire a Flask l'URL dal nome della funzione, passando le parti variabili come argomenti, 
invece di doverlo ricordare e scrivere manualmente.

Cambiare la rotta in un posto si riflette automaticamente ovunque.

I percorsi generati sono sempre assoluti, il che aiuta a evitare errori causati dall'uso di percorsi relativi.

Gestisce automaticamente i caratteri speciali (es. %20 per gli spazi)."""


if __name__=='__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)

