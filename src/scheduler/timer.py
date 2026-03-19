"""
Background Timer Service for scheduled dispensing.
"""

import threading
import time
from datetime import datetime, time as dt_time
from dispenser import Dispenser

class TimerService:
    def __init__(self, config):
        self.config = config
        self.dispenser = Dispenser(config)
        self.running = False
        self.thread = None

    def start(self):
        """Start the timer service in a background thread."""
        self.running = True
        self.thread = threading.Thread(target=self._run_timer)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        """Stop the timer service."""
        self.running = False
        if self.thread:
            self.thread.join()

    def _run_timer(self):
        """Main timer loop."""
        while self.running:
            current_time = datetime.now().time()
            schedule = self.config.get_schedule()

            for entry in schedule:
                schedule_time = dt_time.fromisoformat(entry['time'])
                if self._times_match(current_time, schedule_time):
                    self.dispenser.dispense(entry['compartments'])

            time.sleep(60)  # Check every minute

    def _times_match(self, current, scheduled):
        """Check if current time matches scheduled time (within 1 minute)."""
        return (abs((current.hour * 60 + current.minute) -
                   (scheduled.hour * 60 + scheduled.minute)) <= 1)