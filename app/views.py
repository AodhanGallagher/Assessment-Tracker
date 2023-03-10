# Importing the relevant modules
from flask import render_template, flash, request, redirect, url_for
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from .forms import AssessmentForm
from .models import Assessments

# The route for the main page of the application
@app.route('/', methods=['GET', 'POST'])
def all_assessments():
    form = AssessmentForm()
    # Handles adding a new record to the database with all of the relevant data from the form
    if form.validate_on_submit():
        m = Assessments()
        m.title = form.titleField.data
        m.module_code = form.moduleField.data
        m.deadline = form.deadlineField.data
        m.description = form.descriptionField.data
        m.complete = form.completeField.data
        db.session.add(m)
        db.session.commit()
        form = AssessmentForm(formdata=None) # Creating a blank form with no data

    # Getting all the records from the database to be displayed in the table
    cursor = db.engine.execute('SELECT * FROM assessments ORDER BY deadline ASC')
    items = cursor.fetchall()

    return render_template('all_assessments.html',
                           title='All Assessments',
                           form=form,
                           items=items)

# The route for the completed assessments page of the application
@app.route('/completed_assessments', methods=['GET', 'POST'])
def completed_assessments():
    form = AssessmentForm()
    # Handles adding a new record to the database with all of the relevant data from the form
    if form.validate_on_submit():
        m = Assessments()
        m.title = form.titleField.data
        m.module_code = form.moduleField.data
        m.deadline = form.deadlineField.data
        m.description = form.descriptionField.data
        m.complete = form.completeField.data
        db.session.add(m)
        db.session.commit()
        form = AssessmentForm(formdata=None) # Creating a blank form with no data

    # Getting all the records from the database to be displayed in the table
    cursor = db.engine.execute('SELECT * FROM assessments WHERE complete = 1 ORDER BY deadline ASC')
    items = cursor.fetchall()

    return render_template('completed_assessments.html',
                           title='Completed Assessments',
                           form=form,
                           items=items)

# The route for the incomplete assessments page of the application
@app.route('/incomplete_assessments', methods=['GET', 'POST'])
def incomplete_assessments():
    form = AssessmentForm()
    # Handles adding a new record to the database with all of the relevant data from the form
    if form.validate_on_submit():
        m = Assessments()
        m.title = form.titleField.data
        m.module_code = form.moduleField.data
        m.deadline = form.deadlineField.data
        m.description = form.descriptionField.data
        m.complete = form.completeField.data
        db.session.add(m)
        db.session.commit()
        form = AssessmentForm(formdata=None) # Creating a blank form with no data

    # Getting all the records from the database to be displayed in the table
    cursor = db.engine.execute('SELECT * FROM assessments WHERE complete = 0 ORDER BY deadline ASC')
    items = cursor.fetchall()

    return render_template('incomplete_assessments.html',
                           title='Incomplete Assessments',
                           form=form,
                           items=items)

# The route to handle marking assessments as complete. It updates the complete field on the database to reflect this
@app.route('/flip', methods=['POST'])
def flip():
    a = Assessments.query.filter_by(id=request.form["flip"]).first_or_404()
    a.complete = 1
    db.session.commit()
    return redirect(url_for('incomplete_assessments'))

# The route to handle deleting a record from the database / table
@app.route('/del', methods=['POST'])
def delete():
    a = Assessments.query.filter_by(id=request.form["delete"]).first_or_404()
    db.session.delete(a)
    db.session.commit()
    return redirect(url_for('all_assessments'))