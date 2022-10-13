from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
import os
import pytz

app = Flask(__name__)

db = SQLAlchemy(app)

load_dotenv()

db_host = os.environ['MYSQL_DB_HOST']
db_user = os.environ['MYSQL_DB_USER']
db_password = os.environ['MYSQL_DB_PASSWORD']
db_name = os.environ['MYSQL_DB_NAME']

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{db_user}:{db_password}@{db_host}:3306/{db_name}".format(db_user=db_user, db_password=db_password, db_host=db_host, db_name=db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Todo(db.Model):
    bdt = pytz.timezone('Asia/Dhaka')
    date = datetime.now(bdt)
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=date)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/", methods=['POST', 'GET', 'PUT'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()

            return redirect('/')
        except:
            return "There was an issue"
    elif request.method == 'PUT':
        completed = request.get_json()

        print(completed)

        completed_task = Todo.query.get_or_404(completed["id"])
        completed_task.completed = int(completed["status"])

        try:
            db.session.commit()

            return redirect('/')
        except:
            return "There was an issue"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        print(tasks)
        return render_template("index.html", tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        
        return redirect('/')
    except:
        return "There was an issue"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        task.completed = 0

        try:
            db.session.commit()

            return redirect('/')
        except:
            return "There was an issue"
    else:
        return render_template("update.html", task=task)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)