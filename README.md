# Web Login Flask

A simple web application built with Python and Flask, featuring user authentication, account management, and personal notes.

This project was developed for educational purposes to explore web application development, authentication mechanisms, database integration, and basic security practices.

## Features

- User registration and login
- Password hashing using Werkzeug
- User authentication and session management with Flask-Login
- Google reCAPTCHA integration
- User profile management
- Password and email address updates
- Creating and deleting personal notes
- SQLite database integration using SQLAlchemy

## Technologies

- **Backend:** Python, Flask
- **Database:** SQLite, SQLAlchemy
- **Authentication:** Flask-Login, Werkzeug
- **Security:** Password hashing, Google reCAPTCHA
- **Frontend:** HTML, CSS, JavaScript

## Installation

1. Clone the repository:

   `git clone https://github.com/Ne3x21/Web-Login-Flask.git`

2. Navigate to the project directory:

   `cd Web-Login-Flask`

3. Create a virtual environment:

   `python -m venv venv`

4. Activate the environment:

   Windows: `venv\Scripts\activate`

   Linux/macOS: `source venv/bin/activate`

5. Install the required dependencies.

6. Configure the environment variables using `.env.example`.

7. Run the application:

   `python main.py`

## Security

The application demonstrates several security-related concepts, including password hashing, session-based authentication, and CAPTCHA verification.

This is an educational project and has not undergone a comprehensive security audit. It should not be deployed in a production environment without further security improvements and testing.

## Project Purpose

The main goal of this project is to develop practical skills in Python web development, user authentication, database management, and application security.

## Author

GitHub: [Ne3x21](https://github.com/Ne3x21)
