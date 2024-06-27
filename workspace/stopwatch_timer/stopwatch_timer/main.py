import tkinter as tk
from tkinter import messagebox
from stopwatch import Stopwatch
from history import History

class UI:
    def __init__(self, stopwatch: Stopwatch, history: History):
        self._root = tk.Tk()
        self._root.title("Stopwatch")
        self._stopwatch = stopwatch
        self._history = history

        # UI elements
        self._start_button = tk.Button(self._root, text="Start", command=self._start)
        self._start_button.pack()
        self._stop_button = tk.Button(self._root, text="Stop", command=self._stop, state='disabled')
        self._stop_button.pack()
        self._reset_button = tk.Button(self._root, text="Reset", command=self._reset, state='disabled')
        self._reset_button.pack()
        self._history_button = tk.Button(self._root, text="History", command=self._show_history)
        self._history_button.pack()
        self._time_label = tk.Label(self._root, text="00:00:00.000")
        self._time_label.pack()

    def run(self):
        self._root.mainloop()

    def _start(self):
        self._stopwatch.start()
        self._start_button.config(state='disabled')
        self._stop_button.config(state='normal')
        self._reset_button.config(state='normal')
        self._update_time()

    def _stop(self):
        elapsed_time = self._stopwatch.stop()
        self._start_button.config(state='normal')
        self._stop_button.config(state='disabled')
        self._add_to_history(elapsed_time)
        messagebox.showinfo("Stopped", f"Elapsed time: {self._format_time(elapsed_time)}")

    def _reset(self):
        self._stopwatch.reset()
        self._time_label.config(text="00:00:00.000")
        self._start_button.config(state='normal')
        self._stop_button.config(state='disabled')
        self._reset_button.config(state='disabled')

    def _update_time(self):
        try:
            time = self._stopwatch.get_time()
            self._time_label.config(text=self._format_time(time))
            self._root.after(100, self._update_time)  # Update time every 100ms
        except AttributeError:
            pass  # If stopwatch is not running, do nothing

    def _add_to_history(self, time):
        self._history.add_record(time)

    def _show_history(self):
        records = self._history.get_records()
        if records:
            messagebox.showinfo("History", "\n".join(self._format_time(t) for t in records))
        else:
            messagebox.showinfo("History", "No records found.")

    @staticmethod
    def _format_time(seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int((seconds - int(seconds)) * 1000):03}"

if __name__ == "__main__":
    stopwatch = Stopwatch()
    history = History()
    ui = UI(stopwatch, history)
    ui.run()
