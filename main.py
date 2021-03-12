from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_dynamic>')
def dynamic(page_dynamic):
    return render_template(page_dynamic)


def write_to_csv(data):
    with open('csvfile.csv', mode='a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        name = data['name']
        email = data['email']
        subject = data['subject']
        description = data['description']
        spamwriter.writerow([name, email, subject, description])


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thanks.html')
    else:
        return 'Something Wrong'
