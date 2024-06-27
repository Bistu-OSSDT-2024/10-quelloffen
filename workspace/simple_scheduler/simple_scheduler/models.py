## models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from apscheduler.triggers.date import DateTrigger

# Initialize the SQLAlchemy db instance
db = SQLAlchemy()

class Event(db.Model):
    """Event model representing a single event in the scheduler."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, description, start_time, end_time):
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"<Event {self.title}>"

class Reminder(db.Model):
    """Reminder model representing a reminder for an event."""
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    send_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, event_id, send_time):
        self.event_id = event_id
        self.send_time = send_time

    def __repr__(self):
        return f"<Reminder for Event {self.event_id} at {self.send_time}>"

class EventDAO:
    """Data Access Object for the Event model."""
    @staticmethod
    def add_event(event):
        db.session.add(event)
        db.session.commit()

    @staticmethod
    def delete_event(event_id):
        event = Event.query.get(event_id)
        if event:
            db.session.delete(event)
            db.session.commit()

    @staticmethod
    def get_events_for_day(day):
        return Event.query.filter(
            Event.start_time >= day,
            Event.start_time <= day + datetime.timedelta(days=1)
        ).all()

    @staticmethod
    def update_event(event_id, new_event_data):
        event = Event.query.get(event_id)
        if event:
            event.title = new_event_data.title
            event.description = new_event_data.description
            event.start_time = new_event_data.start_time
            event.end_time = new_event_data.end_time
            db.session.commit()

class ReminderService:
    """Service to handle reminder scheduling and cancellation."""
    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.jobs = {}

    def schedule_reminder(self, reminder):
        job = self.scheduler.add_job(
            self.send_reminder,
            DateTrigger(run_date=reminder.send_time),
            args=[reminder.id],
            id=str(reminder.id)
        )
        self.jobs[reminder.id] = job

    def send_reminder(self, reminder_id):
        # Placeholder for actual reminder logic
        reminder = Reminder.query.get(reminder_id)
        if reminder:
            # Implement the actual reminder logic here
            # For example, sending an email or a notification
            # This is just a placeholder print statement
            print(f"Sending reminder for event {reminder.event_id} at {reminder.send_time}")

    def cancel_reminder(self, reminder_id):
        job = self.jobs.get(reminder_id)
        if job:
            self.scheduler.remove_job(job.id)

# Removed db.create_all() as it should be called in the application entry point
