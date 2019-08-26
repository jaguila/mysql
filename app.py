from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db=SQLAlchemy(app)
class Comment(db.Model):
    __tablename__="comments"
    id=db.Column(db.Integer, primary_key=True)
    content=db.Column(db.String(4096))
comments=[]



SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="patupe",
    password="paSSwoRd1986",
    hostname="patupe.mysql.pythonanywhere-services.com",
    databasename="patupe$comments"
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



@app.route('/', methods=["GET","POST"])
def index():
    if request.method=='GET':
        return render_template('mainpage.html', comments=comments)
    comments.append(request.form['contents'])
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)
