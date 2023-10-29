from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Reemplaza con una clave secreta segura

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        session['nombre'] = nombre  # Guarda el nombre en la sesión
        return redirect(url_for('saludo'))
    return render_template('index.html')

@app.route('/saludo')
def saludo():
    nombre = session.get('nombre', 'Invitado')
    return 'Hola, {}'.format(nombre)

if __name__ == "__main__":
    app.run(debug=True)