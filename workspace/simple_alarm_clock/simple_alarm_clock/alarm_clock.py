import datetime
import threading
import time

class AlarmClock:
    def __init__(self):
        self.time = None
        self.is_set = False
        self.alarm_event = threading.Event()
        self.alarm_thread = None

    def set_alarm(self, time_str: str):
        try:
            self.time = datetime.datetime.strptime(time_str, '%H:%M').time()
            self.is_set = True
            # Removed print statement, UI should handle notifications
        except ValueError as e:
            # This error should be handled by the caller, not printed here
            raise ValueError("Invalid time format") from e

    def start_alarm(self):
        if self.is_set and self.time:
            now = datetime.datetime.now().time()
            target_time = datetime.datetime.combine(datetime.date.today(), self.time)
            if now > self.time:
                target_time += datetime.timedelta(days=1)
            sleep_time = (target_time - datetime.datetime.now()).total_seconds()
            if sleep_time > 0:
                self.alarm_thread = threading.Thread(target=self._wait_and_trigger_alarm, args=(sleep_time,))
                self.alarm_thread.start()
            else:
                # This message should be handled by the UI
                raise ValueError("The set alarm time has already passed for today.")

    def _wait_and_trigger_alarm(self, sleep_time):
        time.sleep(sleep_time)
        if self.is_set:  # Check if the alarm is still set before triggering
            self.alarm_event.set()
            self.alarm_rings()

    def alarm_rings(self):
        # This method can be overridden or replaced by the UI to handle alarm actions
        print("Alarm is ringing!")

    def stop_alarm(self):
        self.is_set = False
        self.alarm_event.clear()
        if self.alarm_thread and self.alarm_thread.is_alive():
            self.alarm_thread.join()  # Wait for the alarm thread to finish if it's running

    # Removed the unused wait_for_alarm method

