## ui.py
from typing import List

from flask import Flask, render_template

class UIService:
    def __init__(self, app: Flask, config=None):
        self.app = app
        self.config = config or {}
        self.template_name = self.config.get('template_name', 'recommendations.html')

    def display_recommendations(self, recommendations: List[dict]):
        """
        Displays travel recommendations through a web interface.
        """
        return self.app.render_template(self.template_name, recommendations=recommendations)

# Example usage:
app = Flask(__name__)
ui_service = UIService(app)

@app.route('/recommendations')
def show_recommendations():
    recommendations = get_recommendations_from_somewhere()  # This is a placeholder for the actual logic
    return ui_service.display_recommendations(recommendations)

# This function should be implemented to fetch recommendations from the RecommendationService
def get_recommendations_from_somewhere():
    # Placeholder for the actual logic to fetch recommendations
    pass
