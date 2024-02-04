# import the path function from django.urls
from django.urls import path

# import the views module from the events app
from .views import EventsView

urlpatterns = [
    # add a URL pattern for the EventsView class
    path('', EventsView.as_view({'get': 'index'}), name='index'),
    # get all events
    path('events/', EventsView.as_view({'get': 'list'}), name='events'),
    # create a new event
    path('events/create/', EventsView.as_view({'post': 'create'}), name='create'),
    # get a event, update a event, delete a event by id
    path('events/<int:pk>/', EventsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='events-detail'),
]
