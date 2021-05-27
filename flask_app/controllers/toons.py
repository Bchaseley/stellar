from flask import render_template, request, redirect
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.toon import Toon
from flask_app.models.user import User

@app.route('/edit_toon/<int:toon_id>')
def edit_toon(toon_id):
    return render_template('edit_toon.html', toon_id = toon_id)