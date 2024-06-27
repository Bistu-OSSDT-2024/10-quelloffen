import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from alarm_clock import AlarmClock

class UI:
    def __init__(self, alarm_clock: AlarmClock):
        self.alarm_clock = alarm_clock
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self._setup_widgets()
        self._start_time_updater()

    def run(self):
        self.root.mainloop()

    def _setup_widgets(self):
        # Time display
        self.time_label = tk.Label(self.root, font=('Helvetica', 48))
        self.time_label.pack(anchor="center")

        # Set alarm button
        self.set_alarm_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm_button_click)
        self.set_alarm_button.pack()

        # Stop alarm button
        self.stop_alarm_button = tk.Button(self.root, text="Stop Alarm", command=self.stop_alarm_button_click, state="disabled")
        self.stop_alarm_button.pack()

    def _start_time_updater(self):
        self.update_time_display()
        self.root.after(1000, self._start_time_updater)  # Update every second

    def update_time_display(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.time_label.config(text=current_time)

    def set_alarm_button_click(self):
        try:
            time_str = self._get_alarm_time_from_user()
            self.alarm_clock.set_alarm(time_str)
            self.set_alarm_button.config(state="disabled")  # Disable the button after setting the alarm
            self.stop_alarm_button.config(state="normal")  # Enable the stop alarm button
        except ValueError as e:
            self._handle_error(str(e))

    def _get_alarm_time_from_user(self):
        from tkinter import simpledialog
        return simpledialog.askstring("Set Alarm", "Enter time (HH:MM):")

    def _handle_error(self, error_message):
        messagebox.showerror("Error", error_message)

    def stop_alarm_button_click(self):
        self.alarm_clock.stop_alarm()
        self.set_alarm_button.config(state="normal")  # Enable the set alarm button again
        self.stop_alarm_button.config(state="disabled")  # Disable the stop alarm button

# This part is to make the UI class work as a standalone script if needed.
if __name__ == "__main__":
    alarm_clock = AlarmClock()
    ui = UI(alarm_clock)
    ui.run()
