from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from ..models.user import User

class Toon:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.class_id = data['class_id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def display_toons(cls, user_id):
        query = 'SELECT * FROM toons JOIN classes ON toons.class_id = classes.id WHERE user_id = %(user_id)s'
        data = {
        'user_id': user_id
        }
        toons = connectToMySQL('stellar').query_db(query, data)
        print(toons)
        return toons

    @classmethod
    def add_toon(cls, data):
        query = 'INSERT INTO toons '