# import the AppConfig class from the django.apps module
from django.apps import AppConfig

# This is the configuration class for the events app
class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "events"
