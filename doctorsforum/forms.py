from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import data_required, length, email, equal_to, Optional, ValidationError
from doctorsforum.models import UserTable

class RegistrationForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = UserTable.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist! Please try different username')

    def validate_email_address(self, email_address_to_check):
        email_address = UserTable.query.filter_by(username=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exist! Please try different email address')

    username = StringField('Username',
                           validators=[data_required(), length(min=3, max=20)])
    email = StringField('Email',
                        validators=[email(), data_required()])
    password1 = PasswordField('Password',
                              validators=[data_required()])
    password2 = PasswordField('Confirm Password',
                              validators=[data_required(), equal_to('password1')])
    submit = SubmitField('SIGN UP')


class ValidationForm(RegistrationForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    name_as_per_mci = StringField(label='Enter your name', validators=[data_required()])
    dropdown_select1 = SelectField(label='place of council', validators=[data_required()],
                                   choices=[('none', 'none'),
                                            ('andhra pradesh medical council', 'andhra pradesh medical council'),
                                            ('arunachal pradesh medical council', 'arunachal pradesh medical council'),
                                            ('assam medical council', 'assam medical council'),
                                            ('bhopal medical council', 'bhopal medical council'),
                                            ('bihar medical council', 'bihar medical council'),
                                            ('bombay medical council', 'bombay medical council'),
                                            ('chandigarh medical council', 'chandigarh medical council'),
                                            ('chattisgarh medical council', 'chattisgarh medical council'),
                                            ('delhi medical council', 'delhi medical council'),
                                            ('goa medical council', 'goa medical council'),
                                            ('gujarat medical council', 'gujarat medical council'),
                                            ('haryana medical council', 'haryana medical council'),
                                            ('himachal pradesh medical council', 'himachal pradesh medical council'),
                                            ('hyderabad medical council', 'hyderabad medical council'),
                                            ('jammu & kashmir medical council', 'jammu & kashmir medical council'),
                                            ('jharkhand medical council', 'jharkhand medical council'),
                                            ('karnataka medical council', 'karnataka medical council'),
                                            ('madhya pradesh medical council', 'madhya pradesh medical council'),
                                            ('madras medical council', 'madras medical council'),
                                            ('mahakoshal medical council', 'mahakoshal medical council'),
                                            ('maharashtra medical council', 'maharashtra medical council'),
                                            ('manipur medical council', 'manipur medical council'),
                                            ('medical council of india', 'medical council of india'),
                                            ('medical council of tanganyika', 'medical council of tanganyika'),
                                            ('mizoram medical council', 'mizoram medical council'),
                                            ('mysore medical council', 'mysore medical council'),
                                            ('nagaland medical council', 'nagaland medical council'),
                                            ('orissa council of medical registration',
                                             'orissa council of medical registration'),
                                            ('pondicherry medical council', 'pondicherry medical council'),
                                            ('punjab medical council', 'punjab medical council'),
                                            ('rajasthan medical council', 'rajasthan medical council'),
                                            ('sikkim medical council', 'sikkim medical council'),
                                            ('tamil nadu medical council', 'tamil nadu medical council'),
                                            ('telangana state medical council', 'telangana state medical council'),
                                            ('travancore cochin medical council, trivandrum',
                                             'travancore cochin medical council, trivandrum'),
                                            ('tripura state medical council', 'tripura state medical council'),
                                            ('uttar pradesh medical council', 'uttar pradesh medical council'),
                                            ('uttarakhand medical council', 'uttarakhand medical council'),
                                            ('vidharba medical council', 'vidharba medical council'),
                                            ('west bengal medical council', 'west bengal medical council')])
    dropdown_select2 = SelectField(label='Year of registration', validators=[data_required()],
                                   choices=[('select year of admission', 'select year of admission'), ('2023', '2023'),
                                            ('2022', '2022'),
                                            ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'),
                                            ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'),
                                            ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'),
                                            ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'),
                                            ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'),
                                            ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'),
                                            ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'),
                                            ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'),
                                            ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'),
                                            ('1985', '1985'), ('1984', '1984'), ('1983', '1983'), ('1982', '1982'),
                                            ('1981', '1981'), ('1980', '1980'), ('1979', '1979'), ('1978', '1978'),
                                            ('1977', '1977'), ('1976', '1976'), ('1975', '1975'), ('1974', '1974'),
                                            ('1973', '1973'), ('1972', '1972'), ('1971', '1971'), ('1970', '1970'),
                                            ('1969', '1969'), ('1968', '1968'), ('1967', '1967'), ('1966', '1966'),
                                            ('1965', '1965'), ('1964', '1964'), ('1963', '1963'), ('1962', '1962'),
                                            ('1961', '1961'), ('1960', '1960'), ('1959', '1959'), ('1958', '1958'),
                                            ('1957', '1957'), ('1956', '1956'), ('1955', '1955'), ('1954', '1954'),
                                            ('1953', '1953'), ('1952', '1952'), ('1951', '1951'), ('1950', '1950'),
                                            ('1949', '1949'), ('1948', '1948'), ('1947', '1947')])
    registration_number = StringField('MCI Registration number', validators=[data_required()])


class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[data_required()])
    password1 = PasswordField('Password',
                              validators=[data_required()])
    # remember_login = BooleanField('remember_me')
    submit = SubmitField('LOGIN')
