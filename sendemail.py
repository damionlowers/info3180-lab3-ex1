from flask import Flask,request,redirect,abort,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
import smtplib

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# @app.route('/')
# def index():
# 	return render_template('index.html');

# Mailing Code Start
from_addr = 'damion.lowers@gmail.com'
to_addr  = 'david@someemail.com'
from_name = 'Damion E. Lowers'
to_name = 'david'
subject = ''
message = """
From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, message)
# Credentials (if needed)
username = ''
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()
# Mailing Code End 


if __name__ == '__main__':
    manager.run()