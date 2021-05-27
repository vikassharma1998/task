from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="nettech")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE batch(name VARCHAR(255),address VARCHAR(255),rno int)")
mycursor.execute("SHOW TABLES")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:////robo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Robo(db.Model):
    Sno = db.Column(db.Integer,primary_key=True)
    Name= db.Column(db.String(50),nullable=False)
    email= db.Column(db.String(50),nullable=False)
    Date_created = db.Column(db.DateTime,default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.Name}"
@app.route('/')
def index():
    robo =Robo(Name='first name',email='first email')
    db.session.ad(robo)
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)    