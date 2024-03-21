
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    lessons = Lesson.query.all()
    return render_template('lessons.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    return render_template('lesson.html', lesson=lesson)

@app.route('/lesson/<int:lesson_id>/quiz')
def quiz(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    return render_template('quiz.html', lesson=lesson)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
