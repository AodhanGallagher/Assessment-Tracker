# Importing the relevant modules
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

# Creating the form that will be used for entering data into the database
class AssessmentForm(FlaskForm):
    titleField = StringField('Assessment Title', validators=[DataRequired(), Length(min=1, max=35, message="Title cannot exceed 30 characters")])
    moduleField = StringField('Module Code', validators=[DataRequired(), Length(min=1, max=10, message="Module code cannot exceed 10 characters")])
    deadlineField = DateField('Deadline', validators=[DataRequired()])
    descriptionField = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=125, message="Description cannot exceed 125 characters")])
    completeField = BooleanField('Complete?')
    submitField = SubmitField('Submit')