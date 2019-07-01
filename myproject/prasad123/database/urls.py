from django.conf.urls import url
from database import views

urlpatterns = [
    url("",views.counter)
]