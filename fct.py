import flask, flask.views
from flask import render_template
from flask import session, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin, BaseView, expose
import os

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
db = SQLAlchemy(app)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.String(30))
    food_and_desc = db.Column(db.String(255))
    alternate_name = db.Column(db.String(255))
    water = db.Column(db.String(10))
    energy = db.Column(db.String(10))
    protein = db.Column(db.String(10))
    fat = db.Column(db.String(10))
    carb = db.Column(db.String(10))
    crude_fiber = db.Column(db.String(10))
    ash = db.Column(db.String(10))
    calcium = db.Column(db.String(10))
    phosphorus = db.Column(db.String(10))
    iron = db.Column(db.String(10))
    retinol = db.Column(db.String(10))
    bcarotene = db.Column(db.String(10))
    vitamina = db.Column(db.String(10))
    thiamin = db.Column(db.String(10))
    riboflavin = db.Column(db.String(10))
    niacin = db.Column(db.String(10))
    ascorbic_acid = db.Column(db.String(10))

def __init__(self, food_id, food_and_desc, alternate_name, water, energy, protein, fat, carb, crude_fiber, ash, calcium, phosphorus, iron, retinol, bcarotene, vitamina, thiamin, riboflavin, niacin, ascorbic_acid):
    self.food_id = food_id
    self.food_and_desc = food_and_desc
    self.alternate_name = alternate_name
    self.water = water
    self.energy = energy
    self.protein = protein
    self.fat = fat
    self.carb = carb
    self.crude_fiber = crude_fiber
    self.ash = ash
    self.calcium = calcium
    self.phosphorus = phosphorus
    self.iron = iron
    self.retinol = retinol
    self.bcarotene = bcarotene
    self.vitamin_a = vitamin_a
    self.thiamin = thiamin
    self.riboflavin = riboflavin
    self.niacin = niacin
    self.ascorbic_acid = ascorbic_acid

# Admin ModelView
class IngAdmin(sqla.ModelView):
    column_display_pk = True
    
    # form_columns = ['nickname', 'description', 'status']
    # # form_overrides = dict(status=SelectField)
    # # form_args = dict(
    # #          status=dict(
    # #             choices=[('Approved', 'Approved'), ('Pending', 'Pending')]
    # #             ))

admin = Admin(app)
admin.add_view(IngAdmin(Ingredient, db.session))

@app.route('/', methods=['GET', 'POST'])
def facebook_login():
	a = Ingredient.query.all()
    	return flask.render_template('index.html',count=17, ing=a)

@app.route('/create', methods=['GET', 'POST'])
def create_database():
	db.create_all()

	a = Ingredient(food_id='1',food_and_desc='pagkaen',alternate_name='1',water='1',energy='1',protein='1',fat='1',carb='1',
		crude_fiber='1',ash='1',calcium='1',phosphorus='1',iron='1',retinol='1',bcarotene='1',vitamina='1',thiamin='1',
		riboflavin='1',niacin='1',ascorbic_acid='1')
	db.session.add(a)
	db.session.commit()

    	return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run()