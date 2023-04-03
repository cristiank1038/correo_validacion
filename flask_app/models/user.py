from flask_app.config.mysqlconnection import connectToMySQL

import re 

#crear una expresión regular para verificar que tengamos el email con formato correcto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#crear una expresion regular para verificar que tengamos el imail con formato correto

from flask import flash
#flash manda mensajes a la plantilla

class User:

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO emails (email) VALUES (%(email)s)"
        result = connectToMySQL('email_validado').query_db(query, formulario)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        results = connectToMySQL('email_validado').query_db(query)
        emails = []
        
        for row in results:
            emails.append( cls(row)) 
        return emails

    @classmethod
    def destroy(cls, formulario):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        result = connectToMySQL('email_validado').query_db(query, formulario)
        return result


    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
        
    
        if not EMAIL_REGEX.match(formulario['email']): 
            flash('Email invalido', 'registro')
            es_valido = False

        query = "SELECT * FROM emails WHERE email = %(email)s"
        results = connectToMySQL('email_validado').query_db(query, formulario)
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False

        return es_valido
