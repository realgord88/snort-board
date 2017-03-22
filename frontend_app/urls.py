from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from frontend_app import views

from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^$', views.home, name='home'),
]

