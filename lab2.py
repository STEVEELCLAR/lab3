from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class addForm(FlaskForm):
    id = StringField(validators=[DataRequired()])
    lname = StringField( validators=[DataRequired()])
    fname = StringField(validators=[DataRequired()])
    course = StringField(validators=[DataRequired()])
    year = StringField( validators=[DataRequired()])
    gender = StringField(validators=[DataRequired()])
    submit = SubmitField('Enter')


class updForm(FlaskForm):
    id = StringField(validators=[DataRequired()])
    newid = StringField(validators=[DataRequired()])
    lname = StringField(validators=[DataRequired()])
    newlname = StringField(validators=[DataRequired()])
    fname = StringField(validators=[DataRequired()])
    newfname = StringField(validators=[DataRequired()])
    course = StringField(validators=[DataRequired()])
    newcourse = StringField(validators=[DataRequired()])
    year = StringField(validators=[DataRequired()])
    newyear = StringField(validators=[DataRequired()])
    gender = StringField(validators=[DataRequired()])
    newgender = StringField(validators=[DataRequired()])
    submit = SubmitField('Enter')

class searchform(FlaskForm):
    info = StringField(validators=[DataRequired()])
    submit = SubmitField('Enter')


