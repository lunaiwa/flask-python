from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/Trimester-1/')
def kangaroos():
    return render_template("Trimester-1.html")

@app_projects.route('/Trimester-2/')
def walruses():
    return render_template("Trimester-2.html")

@app_projects.route('/Trimester-3/')
def hawkers():
    return render_template("Trimester-3.html")