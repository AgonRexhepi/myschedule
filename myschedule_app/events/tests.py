# import TestCase from django.test
from django.test import TestCase
# import reverse from django.urls
from django.urls import reverse
# import status from rest_framework
from rest_framework import status
# import Event model from models
from .models import Event


class EventModelTest(TestCase):
    '''Test module for Event model'''
    @classmethod
    def setUp(self):
        '''Create an event object for testing'''
        self.event = Event.objects.create(
            title='Python Course',
            description='Python Course with Mr. John',
            start_data_time='2024-02-03T12:00:00Z',
            end_data_time='2024-02-03T14:00:00Z'
        )
    
    def test_event_model(self):
        '''Test the event model'''
        self.assertEqual(self.event.title, 'Python Course')
        self.assertEqual(self.event.description, 'Python Course with Mr. John')
        self.assertEqual(self.event.start_data_time, '2024-02-03T12:00:00Z')
        self.assertEqual(self.event.end_data_time, '2024-02-03T14:00:00Z')

class PostEventTest(TestCase):
    '''Test module for creating a new event'''
    def setUp(self):
        '''Create a new event for testing'''
        self.valid_event = {
            "title": "Django Course",
            "description": "Django Course with Mr. Smith",
            "start_data_time": "2024-02-03T12:00:00Z",
            "end_data_time": "2024-02-03T14:00:00Z"
        }
        self.invalid_event = {
            "title": "Django Course",
            "description": "Django Course with Mr. Smith",
            "start_data_time": "2024-02-03T12:00:00Z"
        }
    
    def test_create_valid_event(self):
        '''Test the creation of a new valid event'''
        response = self.client.post(reverse('create'), self.valid_event, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_event(self):
        '''Test the creation of a new invalid event'''
        response = self.client.post(reverse('create'), self.invalid_event, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetEventTest(TestCase):
    '''Test module for getting an event'''
    def setUp(self):
        '''Create an event for testing'''
        self.event = Event.objects.create(
            title='Python Course',
            description='Python Course with Mr. John',
            start_data_time='2024-02-03T12:00:00Z',
            end_data_time='2024-02-03T14:00:00Z'
        )
    
    def test_get_valid_event(self):
        '''Test the get event method'''
        response = self.client.get(reverse('events-detail', kwargs={'pk': self.event.pk}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_invalid_event(self):
        '''Test the get event method with an invalid event id'''
        response = self.client.get(reverse('events-detail', kwargs={'pk': 30}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_all_events(self):
        '''Test the get all events method'''
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UpdateEventTest(TestCase):
    '''Test module for updating an event'''
    def setUp(self):
        '''Create an event for testing'''
        self.event = Event.objects.create(
            event_id=1,
            title='Python Course',
            description='Python Course with Mr. John',
            start_data_time='2024-02-03T12:00:00Z',
            end_data_time='2024-02-03T14:00:00Z'
        )
        self.valid_event = {
            "title": "Django Course",
            "description": "Django Course with Mr. Smith",
            "start_data_time": "2024-02-03T12:00:00Z",
            "end_data_time": "2024-02-03T14:00:00Z"
        }
        self.invalid_event = {
            "title": "Django Course",
            "description": "Django Course with Mr. Smith",
            "start_data_time": "2024-02-03T12:00:00Z"
        }

    def test_update_valid_event(self):
        '''Test the update event method with a valid event id'''
        response = self.client.put(reverse('events-detail', kwargs={'pk': self.event.pk}), self.valid_event,content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_invalid_event(self):
        '''Test the update event method with an invalid event id'''
        response = self.client.put(reverse('events-detail', kwargs={'pk': 30}), self.invalid_event,content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class DeleteEventTest(TestCase):
    '''Test module for deleting an event'''
    def setUp(self):
        '''Create an event for testing'''
        self.event = Event.objects.create(
            event_id=1,
            title='Python Course',
            description='Python Course with Mr. John',
            start_data_time='2024-02-03T12:00:00Z',
            end_data_time='2024-02-03T14:00:00Z'
        )
    
    def test_delete_valid_event(self):
        '''Test the delete event method with a valid event id'''
        response = self.client.delete(reverse('events-detail', kwargs={'pk': self.event.pk}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_invalid_event(self):
        '''Test the delete event method with an invalid event id'''
        response = self.client.delete(reverse('events-detail', kwargs={'pk': 30}), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)