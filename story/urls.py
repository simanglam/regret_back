from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import getStory

router = routers.DefaultRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
    #path('api/v1/', include(router.urls)),

urlpatterns = [
    path('', getStory),
    path('/', getStory),
]
