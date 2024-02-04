# import the models module from the django.db package
from django.db import models

class Event(models.Model):
    # Model for an event with a title, description, start data time, and end data time
    # created_at and updated_at are automatically created and updated when a new event is created or an existing event is updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # primary key for the event
    event_id = models.AutoField(primary_key=True)
    # title of the event (max length 200 characters)
    title = models.CharField(max_length=200)
    # description of the event (max length 500 characters)
    description = models.TextField(max_length=500, blank=True, null=True)
    # start and end times of the event
    start_data_time = models.DateTimeField()
    # end date and time of the event
    end_data_time = models.DateTimeField()


    def __str__(self):
        # return the title of the event
        return self.title
