from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////customers.db'
db = SQLAlchemy(app)

class Custormer(db.Model):
    id= db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(120),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    checkopt1 = db.Column(db.Boolean,nullable = True,default=False)
    checkopt2 = db.Column(db.Boolean,nullable = True,default=False)
    checkopt3 = db.Column(db.Boolean,nullable = True,default=False)
    message = db.Column(db.String,nullable = False)



@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('inlineFormInputName2')
        email = request.form.get('inlineFormInputGroupUsername2')
        if request.form.get('checkopt1') != None:
            checkopt1 =True
        if request.form.get('checkopt1') != None:
            checkopt2 =True
        if request.form.get('checkopt1') != None:
            checkopt3 = True
        message = request.form['comment']

        cu = Custormer(name = name,email = email,checkopt1 = checkopt1,checkopt2=checkopt2,checkopt3=checkopt3,message=message)
        db.session.add(cu)
        db.session.commit()

    return render_template("home.html")


if __name__ == '__main__':
    app.run()