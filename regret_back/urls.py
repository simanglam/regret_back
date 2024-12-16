"""
URL configuration for regret_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from .settings import BASE_DIR
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('story', include('story.urls')),
    re_path(r'^(?P<images>.*)$', lambda request, **kwargs: serve(request, kwargs["images"], document_root=os.path.join(str(BASE_DIR)))),
]
