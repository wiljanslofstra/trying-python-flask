from flask import render_template, redirect, request
from datetime import datetime
from ..main import app, db
from .models import Form
from .forms import ContactForm

@app.route("/contact", methods=('GET', 'POST'))
def contact():
    contact_form = ContactForm()

    if request.method == 'POST' and contact_form.validate():
        # Create new form model instance
        form = Form()

        form.created_at = datetime.now()

        # Write all form data to the form model
        contact_form.populate_obj(form)

        # Add the change to the 'queue'
        db.session.add(form)

        # Insert it into the database
        db.session.commit()

        return redirect('/contact-success')

    return render_template('contact/index.html', form=contact_form)

@app.route("/contact-success")
def contact_success():
    return render_template('contact/success.html')
