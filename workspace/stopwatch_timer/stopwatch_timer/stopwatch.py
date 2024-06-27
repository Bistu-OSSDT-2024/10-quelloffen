import time
from threading import Thread, Event

## stopwatch.py
class Stopwatch:
    """A simple stopwatch implementation that can start, stop, and reset the time."""
    
    def __init__(self):
        self._start_time = None
        self._elapsed_time = 0.0
        self._running = False
        self._event = Event()
    
    def start(self):
        """Start the stopwatch."""
        if not self._running:
            self._start_time = time.time()
            self._running = True
            # Start a thread to update the elapsed time
            Thread(target=self._update_time, args=(self._event,)).start()
    
    def _update_time(self, event):
        """Thread function to update the elapsed time."""
        while self._running and not event.is_set():
            self._elapsed_time = time.time() - self._start_time
            time.sleep(0.1)  # Update every 100ms
    
    def stop(self):
        """Stop the stopwatch and return the elapsed time."""
        if self._running:
            self._event.set()  # Signal the thread to stop
            self._running = False
            self._event.clear()  # Reset the event for future use
            return self._elapsed_time
    
    def reset(self):
        """Reset the stopwatch."""
        self._start_time = None
        self._elapsed_time = 0.0
        self._running = False
    
    def get_time(self):
        """Get the current elapsed time without stopping the stopwatch."""
        if self._running:
            return time.time() - self._start_time + self._elapsed_time
        return self._elapsed_time
