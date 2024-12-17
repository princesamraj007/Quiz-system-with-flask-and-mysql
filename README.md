This is an MCQ quiz application built using Flask and MySQL. Users can take a timed quiz, with randomly selected questions, and their responses are stored in the database. At the end of the quiz, users can view their scores.

Features
User registration with Name and Email
A timer for the quiz session
Randomized, non-repeating questions
Score calculation and response tracking
Database integration using MySQL


Technologies Used
Flask (Web framework)
MySQL (Database)
HTML/CSS (Frontend)
JavaScript (For timer functionality)


Prerequisites
Before you can run this project, make sure you have the following installed:
Python 3.x
MySQL Database
pip (Python package manager)


Set up MySQL Database

Create a new database in MySQL:

CREATE DATABASE quenans;

Create the required tables in MySQL:

CREATE TABLE Questions (
    QuestionID INT AUTO_INCREMENT PRIMARY KEY,
    QuestionText TEXT,
    OptionA TEXT,
    OptionB TEXT,
    OptionC TEXT,
    OptionD TEXT,
    CorrectOption CHAR(1)
);

CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    EmailID VARCHAR(100),
    Score INT
);

CREATE TABLE Responses (
    ResponseID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    QuestionID INT,
    Answer CHAR(1),
    IsCorrect BOOLEAN,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID)
);


Insert sample data for questions in the Questions table. You can use the following example for your Questions table:

INSERT INTO Questions (QuestionText, OptionA, OptionB, OptionC, OptionD, CorrectOption) 
VALUES
('What is the capital of France?', 'Paris', 'Berlin', 'Rome', 'Madrid', 'A'),
('What is 2 + 2?', '3', '4', '5', '6', 'B');


Configure Flask Application

In the app.py file, make sure the MySQL connection details are correct:

db = mysql.connector.connect(
    host="localhost",
    user="root",  # Your MySQL username
    password="1234",  # Your MySQL password
    database="quenans"  # Your database name
)

Run the Flask Application
To start the application, run the following command:

python app.py
