# import render from django.shortcuts
from django.shortcuts import render
# import the Response and status from rest_framework.response
from rest_framework.response import Response
# import status from rest_framework
import rest_framework.status as status
# import the viewsets module from rest_framework
from rest_framework import status, viewsets
# import the Event model
from .models import Event
# import the EventsSerializer
from .serializers import EventsSerializer
# import the AllowAny permission class from rest_framework.permissions
from rest_framework.permissions import AllowAny

class EventsView(viewsets.ViewSet):
    '''View for the Event model'''
    # set the permission classes to AllowAny for all methods
    permission_classes = [AllowAny]
    
    def index(self,request):  
        '''This method is used to get all events'''
        events = Event.objects.all()
        context = {
            "events":events,
        }
        # return all events to the index.html page 
        return render(request,'index.html',context)
        
    def list(self, request):
        '''This method is used to get all events'''
        events = Event.objects.all()
        serializer = EventsSerializer(events, many=True)
        events = []
        for event in serializer.data:
            events.append({
                "id": event["event_id"],
                "title": event["title"],
                "description": event["description"],
                "start": event["start_data_time"],
                "end": event["end_data_time"]
            })
            # return all events
        return Response(data=events, status=status.HTTP_200_OK)
    
    def create(self, request):
        '''This method is used to create a event'''
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # event is added successfully
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # event is not added successfully
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        '''This method is used to get a event by id'''
        try:
            # get the event by id
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            # event not found
            return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Event not found"})
        serializer = EventsSerializer(event)
        # return the event by id
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        '''This method is used to update a event by id'''
        try:
            # get the event by id
            event = Event.objects.get(event_id=pk)
        except Event.DoesNotExist:
            # event not found
            return Response("Event not found!", status=status.HTTP_404_NOT_FOUND)
        serializer = EventsSerializer(event, data=request.data)
        # check if the event is valid
        if serializer.is_valid():
            # save the event
            serializer.save()
            # return the updated event if the event is valid
            return Response(serializer.data)
        # return error message if the event is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        '''This method is used to delete a event by id '''
        try:
            # get the event by id
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            # event not found
            return Response("Event not found!", status=status.HTTP_404_NOT_FOUND)
        if event:
            # delete the event
            event.delete()
        # return a success message if the event is deleted
        return Response("Event succsesfully deleted!", status=status.HTTP_200_OK)
        