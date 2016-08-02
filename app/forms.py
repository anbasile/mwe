from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class tryForm(Form):
    solution = StringField('solution', validators=[DataRequired()])
