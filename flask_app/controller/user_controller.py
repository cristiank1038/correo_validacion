from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods = ['post'])
def log():
    if not User.valida_usuario(request.form):
        return redirect('/')

    User.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    
    return render_template("success.html", emails = User.get_all())


@app.route('/destroy/<int:id>')
def destroy_Email(id):

    data ={
        "id": id
    }
    User.destroy(data)
    return redirect('/success')