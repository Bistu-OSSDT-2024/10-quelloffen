import logging
from config import Config  # Assuming a Config class that holds shared configuration
from weather_service import WeatherService
from traffic_service import TrafficService
from recommendation_service import RecommendationService
from ui import UIService
from notifications_service import NotificationsService
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.ERROR)

class TravelAdvisor:
    def __init__(self,
                 weather_service=WeatherService(),
                 traffic_service=TrafficService(),
                 recommendation_service=RecommendationService(),
                 ui_service=UIService(),
                 notifications_service=NotificationsService()):
        self.weather_service = weather_service
        self.traffic_service = traffic_service
        self.recommendation_service = recommendation_service
        self.ui_service = ui_service
        self.notifications_service = notifications_service

    def start(self):
        try:
            weather_data = self.weather_service.get_weather()
            traffic_data = self.traffic_service.get_traffic()
            recommendations = self.recommendation_service.get_recommendations(weather_data, traffic_data)
            self.ui_service.display_recommendations(recommendations)
            self.notifications_service.send_notifications(weather_data)
        except RequestException as e:
            logging.error(f"An error occurred while fetching data: {e}")
            # Handle the error appropriately, e.g., show an error message to the user
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            # Additional error handling or notifications can be implemented here

def main():
    # Assuming Config holds any shared configuration that needs to be passed around
    config = Config()
    travel_advisor = TravelAdvisor(
        weather_service=WeatherService(config),
        traffic_service=TrafficService(config),
        recommendation_service=RecommendationService(config),
        ui_service=UIService(config),
        notifications_service=NotificationsService(config)
    )
    travel_advisor.start()

if __name__ == '__main__':
    main()
