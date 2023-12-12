from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

species = ["cat", "dog", "porcupine"]


class PetForm(FlaskForm):
    """Form for adding pets"""
    name = StringField("Pet name", validators=[
                       InputRequired(message="Name is required")])
    specie = SelectField("Species", choices=[(sp, sp) for sp in species], validators=[
                         InputRequired(message="Species is required")])
    photo_url = StringField("Photo URL", validators=[
                            Optional(), URL(message="Invalid URL")])
    age = IntegerField("Age", validators=[Optional(), NumberRange(
        min=0, max=30, message="Age must be between 0 and 30")])
    notes = TextAreaField("Comments")


class EditPetForm(FlaskForm):
    """Edit Pet form"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional()])
    available = BooleanField("Available")
