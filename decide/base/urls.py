from django.urls import path
from .views import BaseView
from authentication import views

urlpatterns = [
    path('', BaseView.as_view()),
               ]
