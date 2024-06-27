import requests
from requests.exceptions import RequestException
import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.ERROR)

class NotificationsService:
    def __init__(self, config=None):
        self.config = config or {}
        self.notifications_api_url = self.config.get('notifications_api_url', 'http://api.notifications.com')
        self.api_key = self.config.get('notifications_api_key', 'default_api_key')
        self.default_recipients = self.config.get('default_recipients', [])

    def send_notifications(self, weather_changes: Dict):
        """
        Sends out notifications to alert users of weather changes.

        Args:
            weather_changes (Dict): A dictionary containing the changes in weather.
        """
        try:
            # Prepare the notification data
            notification_data = {
                'weather_changes': weather_changes,
                'recipients': self.default_recipients
            }
            
            # Assuming the API requires JSON data
            headers = {'Content-Type': 'application/json'}
            response = requests.post(f"{self.notifications_api_url}/send", json=notification_data, headers=headers, auth=(self.api_key, ''))
            response.raise_for_status()
            
            # If successful, log the result
            logging.info("Notifications sent successfully.")
        except RequestException as e:
            logging.error(f"An error occurred while sending notifications: {e}")
            # Handle the error appropriately, e.g., retry logic or alerting an admin

# Example usage:
# notifications_service = NotificationsService()
# notifications_service.send_notifications(weather_data)
