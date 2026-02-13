from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    # El mensaje personalizado que aparecerá primero
    return render_template('index.html', mensaje="Hola, te sonara loco, pero "
                                                 "sigues estando en mi cabeza todo un siempre, por eso "
                                                 "hice esto pa ti, recuerdo exactamente todo incluso hasta las "
                                                 "musicas que alguna vez me enseñaste con toda la alegria u.u, no sigo "
                                                 "haciendo cosas para que me quieras, sino para que sepas que te quiero :), "
                                                 "por si te lo preguntas aun si y con todo el corazon jaja")

@app.route('/sorpresa')
def sorpresa():
    return render_template('ventana.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)

