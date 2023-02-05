from flask import render_template, redirect, url_for, flash, request
from functools import wraps
from doctorsforum import app, login_manager
from doctorsforum.forum_urls import app_forum
from doctorsforum.blog_urls import app_blog
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from doctorsforum.forms import RegistrationForm, ValidationForm, LoginForm
from doctorsforum.models import UserTable
from doctorsforum import db
from flask_login import login_user, logout_user, login_required, current_user

council_dict = {'none': 2, 'andhra pradesh medical council': 3, 'arunachal pradesh medical council': 4,
                'assam medical council': 5, 'bhopal medical council': 6, 'bihar medical council': 7,
                'bombay medical council': 8, 'chandigarh medical council': 9, 'chattisgarh medical council': 10,
                'delhi medical council': 11, 'goa medical council': 12, 'gujarat medical council': 13,
                'haryana medical council': 14, 'himachal pradesh medical council': 15, 'hyderabad medical council': 16,
                'jammu & kashmir medical council': 17, 'jharkhand medical council': 18, 'karnataka medical council': 19,
                'madhya pradesh medical council': 20, 'madras medical council': 21, 'mahakoshal medical council': 22,
                'maharashtra medical council': 23, 'manipur medical council': 24, 'medical council of india': 25,
                'medical council of tanganyika': 26, 'mizoram medical council': 27, 'mysore medical council': 28,
                'nagaland medical council': 29, 'orissa council of medical registration': 30,
                'pondicherry medical council': 31, 'punjab medical council': 32, 'rajasthan medical council': 33,
                'sikkim medical council': 34, 'tamil nadu medical council': 35, 'telangana state medical council': 36,
                'travancore cochin medical council, trivandrum': 37, 'tripura state medical council': 38,
                'uttar pradesh medical council': 39, 'uttarakhand medical council': 40, 'vidharba medical council': 41,
                'west bengal medical council': 42}

years_dict = {'select year of admission': 2, '2023': 3, '2022': 4, '2021': 5, '2020': 6, '2019': 7, '2018': 8,
              '2017': 9, '2016': 10, '2015': 11, '2014': 12, '2013': 13, '2012': 14, '2011': 15, '2010': 16,
              '2009': 17, '2008': 18, '2007': 19, '2006': 20, '2005': 21, '2004': 22, '2003': 23, '2002': 24,
              '2001': 25, '2000': 26, '1999': 27, '1998': 28, '1997': 29, '1996': 30, '1995': 31, '1994': 32,
              '1993': 33, '1992': 34, '1991': 35, '1990': 36, '1989': 37, '1988': 38, '1987': 39, '1986': 40,
              '1985': 41, '1984': 42, '1983': 43, '1982': 44, '1981': 45, '1980': 46, '1979': 47, '1978': 48,
              '1977': 49, '1976': 50, '1975': 51, '1974': 52, '1973': 53, '1972': 54, '1971': 55, '1970': 56,
              '1969': 57, '1968': 58, '1967': 59, '1966': 59, '1965': 60, '1964': 61, '1963': 62, '1962': 63,
              '1961': 64, '1960': 66, '1959': 67, '1958': 68, '1957': 69, '1956': 70, '1955': 71, '1954': 72,
              '1953': 73, '1952': 74, '1951': 75, '1950': 76, '1949': 77, '1948': 78, '1947': 79}

posts = [
    {
        'Author': 'Shyam Sagothia',
        'Title': 'Do Hard Work',
        'Content': 'ALL CONTENT HERE',
        'Date': '01/06/2022'
    },
    {
        'Author': 'Yash Desai',
        'Title': 'How To Do Frontend',
        'Content': 'ALL CONTENT HERE',
        'Date': '31/05/2022'
    },
    {
        'Author': 'Yash Desai',
        'Title': 'How To Do Frontend',
        'Content': 'ALL CONTENT HERE',
        'Date': '31/05/2022'
    },
    {
        'Author': 'Yash Desai',
        'Title': 'How To Do Frontend',
        'Content': 'ALL CONTENT HERE',
        'Date': '31/05/2022'
    },
    {
        'Author': 'Yash Desai',
        'Title': 'How To Do Frontend',
        'Content': 'ALL CONTENT HERE',
        'Date': '31/05/2022'
    }
]

app.register_blueprint(app_forum, url_prefix='/forum')
app.register_blueprint(app_blog, url_prefix='/blogs')


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('./templatesloginregister/home.html', title='Home Page')


@app.route('/about')
def about():  # put application's code here
    return render_template('./templatesloginregister/about.html', title='About Page')


@app.route('/forum')
@login_required
def forum():  # put application's code here
    return render_template('./templatesforum/index.html', title='Forum Page')


@app.route('/blogs')
def blogs():  # put application's code here
    return render_template('./templatesblog/index.html', posts=posts, title='Blog Page')


@app.route('/register_page')
def register_main():  # put application's code here
    return render_template('./templatesloginregister/register_main.html', title='Register Page')


@app.route('/login_page')
def login_main():  # put application's code here
    return render_template('./templatesloginregister/login_main.html', title='Login Page')


@app.route('/register_user', methods=['get', 'post'])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_to_create = UserTable(username=form.username.data,
                                   email_address=form.email.data,
                                   password=form.password1.data,
                                   user_role="Normal")
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are noe logged in as: {user_to_create.username}', category='success')
        return redirect(url_for('home'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error with creating a user: {err_msg}", category='danger')
    return render_template('./templatesloginregister/register_user.html', title='User Register Page', form=form)


@app.route('/register_doctor', methods=['get', 'post'])
def register_doc():
    # form1 = RegistrationForm()
    form2 = ValidationForm()
    if form2.validate_on_submit():
        a, b = validating_data(form2.name_as_per_mci.data, form2.registration_number.data, form2.dropdown_select2.data,
                               form2.dropdown_select1.data)
        if "No data available in table" in a or "Showing 0 to 0 of 0 entries" in b:
            flash("Invalid details!! No such doctor in the list of MCI Database!!")
            return render_template('./templatesloginregister/register_doc.html', title='Doctor Register Page',
                                   validation_form=form2)
        else:
            user_to_create = UserTable(username=form2.username.data,
                                       email_address=form2.email.data,
                                       password=form2.password1.data,
                                       user_role="Doctor")
            db.session.add(user_to_create)
            db.session.commit()
            login_user(user_to_create)
            flash(f'Account created successfully! You are noe logged in as: {user_to_create.username}',
                  category='success')
            return redirect(url_for('home'))
    if form2.errors != {}:
        for err_msg in form2.errors.values():
            flash(f"There was an error with creating a user: {err_msg}", category='danger')
    return render_template('./templatesloginregister/register_doc.html', title='Doctor Register Page',
                           validation_form=form2)


@app.route('/login_user', methods=['get', 'post'])
def login_users():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = UserTable.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password1.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('home'))
        else:
            flash('Username or password are not match! Please try again', category='danger')
    return render_template('./templatesloginregister/login_user.html', title='User Login Page', form=form)


@app.route('/login_doctor', methods=['get', 'post'])
def login_doc():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = UserTable.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password1.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('home'))
        else:
            flash('Username or password are not match! Please try again', category='danger')
    return render_template('./templatesloginregister/login_doc.html', title='Doctor Login Page', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("login_main"))


def validating_data(form_name, form_number, form_year, form_council):
    s = Service(executable_path='/home/shyam/PycharmProjects/Doctors-Forum/doctorsforum/chromedriver')
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    web = webdriver.Chrome(service=s, options=option)
    web.get("https://www.nmc.org.in/information-desk/indian-medical-register/")
    name, number, year, council = form_name, form_number, form_year, form_council
    find_by_name = web.find_element(by=By.XPATH, value='//*[@id="doctorName"]')
    find_by_name.send_keys(name)
    find_by_register = web.find_element(by=By.XPATH, value='//*[@id="doctorRegdNo"]')
    find_by_register.send_keys(number)
    find_by_year_click = web.find_element(by=By.XPATH, value='//*[@id="advance_form"]/div[3]/div/div/button')
    find_by_year_click.click()
    find_by_year = web.find_element(by=By.XPATH,
                                    value=f'//*[@id="advance_form"]/div[3]/div/div/ul/li[{years_dict.get(year)}]/a/label/input')
    find_by_year.click()
    find_by_council_click = web.find_element(by=By.XPATH, value='//*[@id="advance_form"]/div[4]/div/div/button')
    find_by_council_click.click()
    find_by_council = web.find_element(by=By.XPATH,
                                       value=f'//*[@id="advance_form"]/div[4]/div/div/ul/li[{council_dict.get(council)}]/a/label/input')
    find_by_council.click()
    submit = web.find_element(value='doctor_advance_Details')
    submit.click()
    print("Running...")
    time.sleep(4)
    fetched_data = []
    text_find = web.find_elements(by=By.XPATH, value='//*[@id="doct_info5"]/tbody/tr')
    for text in text_find:
        fetched_data.append(text.text)

    text_got = web.find_element(by=By.XPATH, value='//*[@id="doct_info5_info"]')
    no_of_result = text_got.text
    web.close()
    return fetched_data, no_of_result


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()
            if ((current_user.role != role) and (role != "ANY")):
                return login_manager.unauthorized()
            return fn(*args, **kwargs)

        return decorated_view

    return wrapper
