# Student-Management-System
A full-stack Student Management System built with Python, Django, and MySQL — supports adding, editing, deleting, and searching student records through a clean web interface.

## Features

Add new student records
Edit and update existing student details
Delete student records
View all student records in a structured table
Search and filter students by name or other fields


## Tech Stack
LayerTechnologyBackendPython, DjangoFrontendHTML, CSS, JavaScriptDatabaseMySQL / SQLite

## Project Structure
student-management-system/
│
├── students/               # Django app
│   ├── models.py           # Student data model
│   ├── views.py            # CRUD logic
│   ├── urls.py             # App URL routing
│   └── templates/          # HTML templates
│
├── static/                 # CSS and JS files
├── manage.py               # Django project manager
├── db.sqlite3              # SQLite database (if used)
├── requirements.txt        # Python dependencies
└── README.md

## Installation & Setup
1. Clone the Repository
bash git clone https://github.com/your-username/student-management-system.git
cd student-management-system
2. Create a Virtual Environment
bashpython -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
3. Install Dependencies
bashpip install -r requirements.txt
4. Configure Database
For SQLite (default), no extra setup needed.
For MySQL, update DATABASES in settings.py:
pythonDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5. Run Migrations
bashpython manage.py makemigrations
python manage.py migrate
6. Start the Development Server
bashpython manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

## Usage

Navigate to the home page to view all student records
Use the Add Student form to create a new record
Click Edit on any record to update student details
Click Delete to remove a student
Use the Search bar to filter students by name or ID


## Author
N. Jhansi Mahalakshmi
B.Tech CSE (AI & ML) — K.V.G. College of Engineering, Sullia
Intern @ Dhee Coding Lab, Bengaluru

## License
This project is for educational purposes.
