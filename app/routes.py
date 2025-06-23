from flask import render_template, abort
from app import app
from app.lessons import LESSONS

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', lessons=LESSONS)

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lesson = next((lesson for lesson in LESSONS if lesson['id'] == lesson_id), None)
    if lesson is None:
        abort(404)
    return render_template('lesson.html', title=lesson['title'], lesson=lesson) 