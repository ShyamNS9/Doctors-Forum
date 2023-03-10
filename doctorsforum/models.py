from doctorsforum import db, login_manager
from doctorsforum import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user):
    data = UserTable.query.filter_by(id=user).first()
    # print(data.id, data.user_role, data.username)
    return data


class UserTable(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False, )
    user_role = db.Column(db.String(80))

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        print("Password check: ", bcrypt.check_password_hash(self.password_hash, attempted_password))
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
