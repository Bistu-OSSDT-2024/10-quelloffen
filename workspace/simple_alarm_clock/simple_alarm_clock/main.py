## main.py
import tkinter as tk
from datetime import datetime
from alarm_clock import AlarmClock
from ui import UI

def main():
    # Initialize the alarm clock
    alarm_clock = AlarmClock()

    # Create the UI and pass the alarm clock instance to it
    root = tk.Tk()
    ui = UI(root, alarm_clock)

    # Run the UI main loop
    ui.run()

if __name__ == "__main__":
    main()
