from flask import render_template
from webapp import webapp

@webapp.route('/')
@webapp.route('/index')
@webapp.route('/profile')
def profile():
    return render_template("index.html")

@webapp.route('/register')
def menu():
    return render_template("games.html")

@webapp.route('/csgo/stats')
def csgo_stats():
    return 0

@webapp.route('/csgo/team')
def csgo_team():
    return 0