from urllib import request
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

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

    return JsonResponse(routes, safe=False)