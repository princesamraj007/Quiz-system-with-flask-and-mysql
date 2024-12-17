from flask import Flask, render_template, request, redirect, session
import mysql.connector
import time
import random


app = Flask(__name__)
app.secret_key = 'mcq_quiz_abcdefg'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="quenans"
)
cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['start_time'] = time.time()
        session['score'] = 0
        session['current_question'] = 1
        return redirect("/quiz")
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if 'answered_questions' not in session:
        session['answered_questions'] = []  

    if len(session['answered_questions']) >= 100 or time.time() - session['start_time'] > 3600:
        return redirect("/result")
    
    elapsed_time = time.time() - session['start_time']
    remaining_time = max(0, 3600 - elapsed_time) 
    remaining_time = round(remaining_time)  

    if request.method == "POST":
        answer = request.form['answer'].strip().upper()
        correct_option = session['current_question_data'][6]  
        
        if answer == correct_option:  
            session['score'] += 1
        
        session['answered_questions'].append(session['current_question_data'][0])  

    placeholders = ', '.join(['%s'] * len(session['answered_questions']))
    query = f"SELECT * FROM Questions WHERE QuestionID NOT IN ({placeholders})" if session['answered_questions'] else "SELECT * FROM Questions"
    cursor.execute(query, tuple(session['answered_questions']))
    questions = cursor.fetchall()

    if not questions:  
        return redirect("/result")
    
    session['current_question_data'] = random.choice(questions)

    return render_template("quiz.html", question=session['current_question_data'], remaining_time=remaining_time)

@app.route("/result")
def result():
    cursor.execute(
        "INSERT INTO Students (Name, EmailID, Score) VALUES (%s, %s, %s)",
        (session['name'], session['email'], session['score'])
    )
    db.commit()

    return render_template("result.html", name=session['name'], score=session['score'])

if __name__ == "__main__":
    app.run(debug=True)
