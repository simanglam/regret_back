from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Story
import json
class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Story
        fields = "__all__"