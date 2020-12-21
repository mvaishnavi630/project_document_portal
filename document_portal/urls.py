"""document_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from document_portal import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name="home"),
    url(r'^test/$', views.TestPage.as_view(), name="test"),
    url(r'^thanks/$', views.ThanksPage.as_view(), name="thanks"),
    url(r'^admin/', admin.site.urls),
    url(r'^portal/', include("portal.urls", namespace="portal")),
    url(r'^portal/', include("django.contrib.auth.urls")),
    url(r'^files/', include("files.urls", namespace="files")),
]
