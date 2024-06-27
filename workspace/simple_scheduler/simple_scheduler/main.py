from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from apscheduler.schedulers.background import BackgroundScheduler
from models import Event, EventDAO, Reminder, ReminderService
from views import *

app = Flask(__name__)
Bootstrap(app)

# Load environment variables from .env file
from python_dotenv import load_dotenv
load_dotenv()

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize the scheduler
scheduler = BackgroundScheduler()

# Register the reminder service with the scheduler
reminder_service = ReminderService(scheduler)

# Define routes and views
app.add_url_rule('/', view_func=IndexView.as_view('index'))

# Initialize the database
db.create_all()

# Start the scheduler
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
