import data_manager
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all-mentors-by-name')
def mentor_names():
    mentor_names = data_manager.get_all_mentors_names()
    return render_template('mentor_names.html', mentor_names=mentor_names)


@app.route('/mentors-from-Miskolc-by-nickname')
def mentor_nicknames():
    mentor_names = data_manager.get_mentors_nicknames('Miskolc')
    return render_template('nicknames.html', mentor_names=mentor_names)


@app.route('/Carol-phonenumber')
def carol_fullname():
    applicant_names = data_manager.get_full_name()
    return render_template('carol_hat.html', applicant_names=applicant_names)


@app.route('/hat-owner-by-email')
def name_by_email():
    applicant_names = data_manager.get_full_name_with_email()
    return render_template('name_by_email.html', applicant_names=applicant_names)


@app.route('/add-new-applicant', methods=['GET', 'POST'])
def add_new_applicant():
    if request.method == 'GET':
        return render_template('new_applicant.html')
    elif request.method == 'POST':

        form_data = {
            'first_name': request.form['first_name'],
            'last_name' : request.form['last_name'],
            'phone_number' : request.form['phone_number'],
            'email' : request.form['email'],
            'application_code': int(54823)
        }

        data_manager.add_new_applicant(form_data)


        new_applicant = data_manager.display_new_applicant(54823)

        return render_template('new_applicant_details.html',
                               new_applicant=new_applicant)

@app.route('/display-all-applicants')
@app.route('/update-applicant')
def display_all_applicants():
    all_applicants = data_manager.list_all_applicants()
    return render_template('all_applicants.html',
                           all_applicants=all_applicants)


@app.route('/update-applicant/<id>')
def update_applicant(id):
    if request.method == 'GET':
        applicant=data_manager.display_applicant(id)
        return render_template('update_applicant.html', applicant=applicant, id=id)
    elif request.method == 'POST':
        form_data = {
            'id': request.form['id'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'phone_number': request.form['phone_number'],
            'email': request.form['email']
        }
        data_manager.update_applicant_data(form_data)
        all_applicants = data_manager.list_all_applicants()
        return render_template('all_applicants.html',
                               all_applicants=all_applicants)


if __name__ == '__main__':
    app.run(debug=True)


