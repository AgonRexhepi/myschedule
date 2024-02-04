#  import the admin module from the django.contrib package
from django.contrib import admin

# import the Event model
from .models import Event

# register the Event model with the admin site
admin.site.register(Event)
