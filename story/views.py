from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpRequest
from rest_framework import viewsets
from .serializers import  StorySerializer
from .models import Story
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

# Create your views here.
    
def getStory(request: WSGIRequest):
    if request.method == 'GET':
        queryset = Story.objects.all().order_by('sold')
        storyId = request.GET.get('id', None)
        if storyId is not None:
            queryset = Story.objects.all().filter(storyId="".join(storyId))
        return JsonResponse(serializers.serialize('json', queryset), safe=False)