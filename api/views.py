from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Story
from . serializers import StorySerializer


# Create your views here.

@api_view(['GET'])
def getRoute(request):

    routes = [
        {
            'Endpoint': '/stories/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/stories/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single story object'
        },
        {
            'Endpoint': '/stories/create/',
            'method': 'POST',
            'title': {'title': ""},
            'author': {'author': ""},
            'body': {'body': ""},
            'description': 'Creates new stories with data sent in post request'
        },
        {
            'Endpoint': '/stories/id/update/',
            'method': 'PUT',
            'title': {'title': ""},
            'author': {'author': ""},
            'body': {'body': ""},
            'description': 'Creates an existing stories with data sent in post request'
        },
        {
            'Endpoint': '/stories/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and existing story'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getStories(request):
    stories = Story.objects.all()
    serializer= StorySerializer(stories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStory(request, pk):
    stories = Story.objects.get(id=pk)
    serializer= StorySerializer(stories, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createStory(request):
    data= request.data
    stories= Story.objects.create(
        title = data['title'],
        author = data['author'],
        description = data['description'],
        body = data['body'],
    )
    serializer = StorySerializer(stories, many= False)
    return Response(serializer.data)