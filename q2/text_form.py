from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, IntegerField, RadioField
from wtforms.validators import DataRequired

class SubmissionForm(FlaskForm):
    first = IntegerField('First', validators=[DataRequired()])
    second = IntegerField('Second', validators=[DataRequired()])
    operation = RadioField('Operation', choices=[('add','Add'),('subtract','Subtract'), ('multiply', 'Multiply'), ('divide', 'Divide')])
    submit = SubmitField('Submit')
