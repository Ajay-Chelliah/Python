from flask import Flask, render_template, request, redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.Integer, default=0)
    Del_location = db.Column(db.String(200), nullable=False)
    Del_Date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Task {self.id}>'

# Routes
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        task_item = request.form['items']
        task_weight = request.form['weight']
        task_loc = request.form['loc']
        task_date = request.form['date']
        new_task = Todo(
            items=task_item, 
            weight=int(task_weight), 
            Del_location=task_loc, 
            Del_Date=datetime.strptime(task_date, '%Y-%m-%d')
        )
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error: {e}")
            return f'Error: {e}'
    else:
        tasks = Todo.query.order_by(Todo.Del_Date).all()
        return render_template('index.html', tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id: int):
    delete_task = Todo.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def update(id: int):
    task = Todo.query.get_or_404(id)
    if request.method == "POST":
        task.items = request.form['items']
        task.weight = int(request.form['weight'])
        task.Del_location = request.form['loc']
        task.Del_Date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Error: {e}")
            return f"Error: {e}"
    else:
        return render_template("edit.html", task=task)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
