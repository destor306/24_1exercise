from flask import Flask, render_template, request, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is stupid"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_pet_adoptions"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)


@app.route('/')
def homepage():
    """This is the homepage"""
    pets = Pet.query.all()
    print(pets)
    return render_template('home.html', pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """This is where you add pet"""
    form = PetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.specie.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"created new pet : name is {name}")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route("/pets/<int:pet_id>")
def diplay_pet(pet_id):
    """Displays pet info detail"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_info.html', pet=pet)


@app.route("/pets/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_form_pet(pet_id):
    """Edit pet info detail"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template('edit_pet_form.html', form=form)
