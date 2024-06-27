## history.py
import json
import os

class History:
    """A class to handle storing and retrieving timing records from a file."""
    
    def __init__(self, file_path='history.json'):
        self._file_path = file_path
        self._records = self._load_records()
    
    def _load_records(self):
        """Load records from the file."""
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file:
                return json.load(file)
        return []
    
    def add_record(self, time):
        """Add a new timing record."""
        self._records.append(time)
        self._save_records()
    
    def _save_records(self):
        """Save records to the file."""
        with open(self._file_path, 'w') as file:
            json.dump(self._records, file, indent=4)
    
    def get_records(self):
        """Get all stored timing records."""
        return self._records
