from db import db
class Login(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(20))
    role_id = db.Column(db.Integer)

    def __init__(self,username,password,role_id):
        self.username = username
        self.password = password
        self.role_id = role_id

db.create_all()
login = Login()
db.session.add(login)
db.session.commit()