from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
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
        emailtoSend = name+ "@"+email
        checkopt1 = False
        checkopt2 = False
        checkopt3 = False
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
        subject = 'Kurs fotografii'
        name = name
        message = message
        recipients = ['vassilli.zaitsev@gmail.com']
        mesage_to_admin = Message(subject=subject,
                                  sender=app.config.get("MAIL_USERNAME"),
                                  recipients=recipients,  # replace with your email for testing
                                  body="Message from: " + name + "\n" + "email: " + email + "\n" + "Message:" + message)
        message_to_sender = Message(subject="Dziękuje za wysłanie wiadomośći",
                                    sender=app.config.get("MAIL_USERNAME"),
                                    recipients=list(emailtoSend.split(" ")), # replace with your email for testing
                                    body="Dziękuję za wiadomość, wkrótce odpiszę")
        mail.send(mesage_to_admin)
        mail.send(message_to_sender)

    return render_template("home.html")

# email configuration
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='vassilli.zaitsev@gmail.com',
    MAIL_PASSWORD='qplzxmdxmzakrwei'
)
mail = Mail(app)
if __name__ == '__main__':
    app.run()